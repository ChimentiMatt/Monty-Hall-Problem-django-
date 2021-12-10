from django.urls import path
from . import views

app_name = 'appMonty'
urlpatterns = [
    path('myview/', views.myview, name='myview')
]