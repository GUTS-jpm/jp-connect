from django.urls import path
from jpconnect import views

app_name = 'jpconnect'

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.home, name='news'),
]
