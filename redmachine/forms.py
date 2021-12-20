from django import forms
from django.db.models import fields
from . import models

class CarForm(forms.ModelForm):
    class Meta:
        model = models.Car
        fields = [
            'title',
            'description',
            'image'
        ]

class CommentCarForm(forms.ModelForm):
    class Meta:
        model = models.CommentCar
        fields = [
            'post',
            'text',
        ]