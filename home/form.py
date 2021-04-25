from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.forms import ModelForm
from . models import TodoItem

from . models import contact

class createuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

	class Meta:
		model = TodoItem
		fields = '__all__'