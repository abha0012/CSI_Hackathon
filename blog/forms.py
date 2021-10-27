from .models import Comment, Document
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document' )