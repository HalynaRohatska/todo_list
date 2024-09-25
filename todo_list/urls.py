from django.urls import path

from todo_list.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_task_status,
    TagListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView
)


app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/toggle/", toggle_task_status, name='toggle-task-status'),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>/", TagsUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", TagsDeleteView.as_view(), name="tag-delete")
]
