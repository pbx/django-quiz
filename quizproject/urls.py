from django.contrib.auth.decorators import login_required
from django.conf.urls import include, url
from django.contrib import admin

from quiz.views import answer_reader, QuestionDetail, QuizDetail, QuizList


urlpatterns = [
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', QuizList.as_view(), name="quiz-list"),
    url(r'^quiz-(?P<pk>\d+)$', 
        login_required(QuizDetail.as_view()), name="quiz-detail"),
    url(r'^question-(?P<pk>\d+)$', 
        login_required(QuestionDetail.as_view()), name="question-detail"),
    url(r'^answer-(?P<question_pk>\d+)$', 
        login_required(answer_reader), name="answer-reader")
    ]
