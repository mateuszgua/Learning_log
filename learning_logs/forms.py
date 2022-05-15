from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Main Class for topic"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text' : ''}


class EntryForm(forms.ModelForm):
    """Main class for entry"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}