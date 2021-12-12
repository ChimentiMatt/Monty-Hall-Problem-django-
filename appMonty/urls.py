from django.urls import path
from . import views

app_name = 'appMonty'
urlpatterns = [
    path('', views.myview, name='myview'),
    path('frontendpost/', views.frontendpost, name='frontendpost'),
    path('get_data', views.get_data, name='get_data')
]