from django import forms


class AnswerForm(forms.Form):
    answer = forms.ChoiceField(widget=forms.RadioSelect, choices=((True, 'True'), (False, 'False')))
    question = forms.IntegerField(widget=forms.HiddenInput)
