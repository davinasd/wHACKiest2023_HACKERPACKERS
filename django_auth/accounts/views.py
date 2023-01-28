# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
from django.shortcuts import redirect

#added for button click
def button_click(request):
    # Code to handle the button click (e.g. saving data to the database)
    return redirect('target_page')

def target_page(request):
    return render(request, 'children.html')
def target_page2(request):
    return render(request, 'family.html')
def button_click2(request):
    # Code to handle the button click (e.g. saving data to the database)
    return redirect('target_page2')
def button_click3(request):
    # Code to handle the button click (e.g. saving data to the database)
    return redirect('target_page3')
def target_page3(request):
    return render(request, 'elder.html')
