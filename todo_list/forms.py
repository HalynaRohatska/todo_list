from django import forms

from todo_list.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.prefetch_related(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"})
    )

    class Meta:
        model = Task
        fields = ("content", "deadline", "tags",)
