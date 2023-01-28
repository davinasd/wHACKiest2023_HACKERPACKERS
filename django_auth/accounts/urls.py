# accounts/urls.py
from django.urls import path

from .views import SignUpView
from . import views


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('button/', views.button_click, name='button'),
    path('button2/', views.button_click2, name='button2'),
    path('button3/', views.button_click3, name='button3'),
    path('children/', views.target_page, name='target_page'),
    path('family/', views.target_page2, name='target_page2'),
    path('elder/', views.target_page3, name='target_page3'),
]