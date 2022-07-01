import re
from django.contrib.auth.models import User
from django import forms

from .models import Profile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    favgenre = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password','favgenre']
    
    def clean(self):
        super(UserForm, self).clean()

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if len(username) < 5:
            self._errors['username'] = self.error_class(['A minimum of 5 characters is required'])

        if len(username) > 15:
            self._errors['username'] = self.error_class(['Up to 15 characters'])

        if len(password) < 6:
            self._errors['password'] = self.error_class(['Password lenght should not be less than 6 characters'])

        if not re.search("[A-Za-z0-9]", password):
            self._errors['password'] = self.error_class(['Password must contain letters and at least one number'])

        return self.cleaned_data


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'favgenre','image',]

			




		
		


