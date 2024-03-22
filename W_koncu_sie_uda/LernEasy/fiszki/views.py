from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def fiszkiapp(request):
    return render(request,template_name='fiszki/fiszki.html')
