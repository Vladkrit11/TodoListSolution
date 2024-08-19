from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    task_toggle_status
)

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('task/add/', TaskCreateView.as_view(), name='task-add'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('task/toggle-status/<int:pk>/', task_toggle_status, name='task-toggle-status'),
    path('tags/', TagListView.as_view(), name='tags'),
    path('tag/add/', TagCreateView.as_view(), name='tag-add'),
    path('tag/update/<int:pk>/', TagUpdateView.as_view(), name='tag-update'),
    path('tag/delete/<int:pk>/', TagDeleteView.as_view(), name='tag-delete'),
]
