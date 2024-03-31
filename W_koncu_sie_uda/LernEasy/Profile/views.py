from django.shortcuts import render

# Create your views here.

def profile_tem(request):
    return render(request,template_name="Profile/Profile.html")