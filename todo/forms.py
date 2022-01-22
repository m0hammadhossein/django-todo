from django import forms
from .models import Todo


class CreateNewTask(forms.ModelForm):

    def save(self, user, commit=True):
        task = super().save(commit=False)
        task.user = user
        task.save()
        return task

    class Meta:
        model = Todo
        exclude = ('user',)