from django.shortcuts import render

# Create your views here.

def WelcomePage(request):
    return render(request,'Welcome.html')