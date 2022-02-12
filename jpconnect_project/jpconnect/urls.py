from django.urls import path
from jpconnect import views

app_name = 'jpconnect'

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('weather/', views.weather, name='weather'),
    path('<slug:name_slug>', views.show_name, name='show_name'),
    path('search/', views.Search, name = 'search'),
]
