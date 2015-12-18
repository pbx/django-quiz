from django import http
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from quiz.models import Quiz, Question, UserAnswer
from quiz.forms import AnswerForm


class QuizList(ListView):
    model = Quiz


class QuizDetail(DetailView):
    model = Quiz
    context_object_name = 'quiz'
    queryset = Quiz.objects.all()

    def first_question(self):
        return self.object.question_set.all()[0]


class QuestionDetail(DetailView):
    model = Question
    context_object_name = 'question'
    queryset = Question.objects.all()

    def get_context_data(self, **kwargs):
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = AnswerForm(initial={'question': self.object})
        return context


def answer_reader(request, question_pk):
    """Process submitted answer and move to next question, or finish"""
    question = Question.objects.get(pk=question_pk)
    answer = {'True': True, 'False': False}[request.POST['answer']]
    user = request.user
    UserAnswer.objects.create(question=question, user=user, answer=answer)
    if answer == question.answer:
        messages.add_message(request, messages.SUCCESS, "Yes! That one was {}.".format(question.answer))
    else:
        messages.add_message(request, messages.WARNING, "Sorry, that one was {}.".format(question.answer))

    if question.next():
        next_question = reverse("question-detail", kwargs={'pk': question.next().pk})
        return http.HttpResponseRedirect(next_question)
    else:
        messages.add_message(request, messages.SUCCESS, "Completed quiz for {}!".format(question.quiz))
        return http.HttpResponseRedirect("/")
