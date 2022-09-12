# TODO: Implement Routings Here

from django.urls import path

from . import views

app_name = 'katalog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]