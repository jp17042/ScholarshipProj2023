from django import forms

class SurveyForm(forms.Form):
    S_name = forms.CharField()
    Q_options = forms.CharField()
    S_question = forms.CharField()