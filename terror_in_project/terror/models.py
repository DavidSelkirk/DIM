from django.db import models
from django import forms
# Create your models here.

class GameForm(forms.ModelForm):
        name = forms.CharField(max_length=50,
                help_text='Please enter your move.')

