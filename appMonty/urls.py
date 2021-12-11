from django.urls import path
from . import views

app_name = 'appMonty'
urlpatterns = [
    path('', views.myview, name='myview'),
    path('postview/', views.fontendpost, name='postview')
]