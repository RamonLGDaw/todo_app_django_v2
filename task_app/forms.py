from django import forms
from task_app.models import Category

class CreateNewTask(forms.Form):
    title = forms.CharField(
        label='Create a new task',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control mt-2 mb-3',
            'placeholder': 'new task...',
            'maxlength': 100
        })
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select a category",
        widget=forms.Select(attrs={
            'class': 'form-select mt-2'
        })
    )