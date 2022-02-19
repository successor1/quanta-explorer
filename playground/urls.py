from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('', views.index),
    path('a/<qaddress>', views.qaddress),
    path('tokens/', views.tokens),
    path('messages/', views.messages),
    path('richlist/', views.rich_list)
]