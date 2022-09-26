from django.urls import path
from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.IndexView.as_view(), name='show_todolist'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('create-task/', views.create_task, name='create_task'),
    path('<int:task_id>/delete-task/', views.delete_task, name='delete_task'),
    path('<int:task_id>/finish-task/', views.finish_task, name='finish_task'),
]