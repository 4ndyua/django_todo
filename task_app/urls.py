from django.urls import path

from task_app.views import TaskListView, TaskCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name='task-list'),
    path("create/", TaskCreateView.as_view(), name="task-create"),

]

app_name = 'task_app'