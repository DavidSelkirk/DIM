from django.db import models
from django import forms
# Create your models here.

class GameForm(forms.Form):
        move = forms.CharField(max_length=10,
                help_text='Please enter your move.')

