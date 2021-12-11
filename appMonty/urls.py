from django.urls import path
from . import views

app_name = 'appMonty'
urlpatterns = [
    path('', views.myview, name='myview'),
    path('frontendpost/', views.frontendpost, name='frontendpost')
]