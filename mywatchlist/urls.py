from django.urls import path
from . import views

app_name = 'mywatchlist'
urlpatterns = [
    path('json/', views.show_json, name='json_format'),
    path('xml/', views.show_xml, name='xml_format'),
    path('html/', views.IndexView.as_view(), name='html_format'),
]