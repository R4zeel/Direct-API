from django.urls import path

from . import views

app_name = 'create_campaign'

urlpatterns = [
    path('', views.index, name='index')
]