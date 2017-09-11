from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email']
        # exclude =['full_name']
    def clean_email(self):
        email= self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain,extension = provider.split(".")
        if not domain=='USC':
            raise forms.ValidationError("Please make sure u use ur USC email")
        if not extension=='edu':
            raise forms.ValidationError("Please use a valid edu email address")
        return email

    def clean_full_name(self):
        full