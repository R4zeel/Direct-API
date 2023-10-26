from django.urls import path

from . import views

app_name = 'create_campaign'

urlpatterns = [
    path('', views.index, name='index'),
    path('ad_groups/', views.ad_group_create, name='ad_groups_create'),
]