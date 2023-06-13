from django import forms

class SurveyForm(forms.Form):
    S_name = forms.CharField(label='Survey Name', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['S_name'].widget.attrs.update({'class': 'survey-name-input'})
