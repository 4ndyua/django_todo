from django import forms
from task_app.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    time_end = forms.SelectDateWidget()

    class Meta:
        model = Task
        fields = "__all__"
