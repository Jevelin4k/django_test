from django import forms
from django.core import  validators




class ForName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_date = super().clean()
        email = all_clean_date['email']
        vmail = all_clean_date['verify_email']

        if email != vmail:
            raise forms.ValidationError("make sure emails match")


    """anti_bot = forms.CharField(required=False,
                               widget=forms.HiddenInput,
                               validators=[validators.MaxLengthValidator(0)])"""


    """def clean_anti_bot(self):
        anti_bot = self.cleaned_data['anti_bot']
        if len(anti_bot) > 0:
            raise forms.ValidationError('GOTCH BOT!')
        return anti_bot"""