from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Famille


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('initials', 'dates', 'bio')
        widgets = {
            'initials': forms.TextInput(attrs={'class': 'form-control'}),
            'dates': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Вы не можете создать такой слаг.')
        return new_slug


class FamilleForm(forms.ModelForm):
    class Meta:
        model = Famille
        fields = ('title', 'details')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Вы не можете создать такой слаг.')
        return new_slug
