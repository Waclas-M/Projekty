from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(requst):
    form = UserCreationForm()
    return render(requst,'users/registrtion.html',{'form':form})