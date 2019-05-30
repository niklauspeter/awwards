from django import forms
from .models import Project, Profile

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user', 'profile']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

