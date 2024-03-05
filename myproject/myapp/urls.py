from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("home",views.home, name="home"),
    path("mydata/<str:param>/", views.mydata, name="mydata"),
    path("users/", views.usersdata, name="userdata"),
    path("contact/", views.contactForm, name="contactForm"),
    path("success/", views.successPage, name="successPage"),
    path("form/", views.myForm, name="myForm"),
    path("next_page/", views.next_page, name="next_page"),
    path('myprofile/', views.myProfile, name='myprofileDet'),
    path('create_user/', views.create_user, name='create_user')
 
]

