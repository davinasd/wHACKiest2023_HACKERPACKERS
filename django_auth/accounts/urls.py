# accounts/urls.py
from django.urls import path

from .views import SignUpView
from . import views


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('button/', views.button_click, name='button'),
    path('children/', views.target_page, name='target_page')
]