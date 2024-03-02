from django.urls import path
from.import views
from.import templates

urlpatterns =[
    path("" ,views.say_hello, name='index'),
    path("secretpage/", views.secretPage, )
]