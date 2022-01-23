from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(required=True)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        rpassword = self.cleaned_data.get('confirm_password')
        if password != rpassword:
            raise ValidationError('Error in confirm your password')
        return rpassword

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username','password')
