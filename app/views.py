from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.


def registration(request):
    ERFO=RegistrationForm()
    d={'ERFO':ERFO}
    if request.method=='POST':
        DRFO=RegistrationForm(request.POST)
        if DRFO.is_valid():
            return HttpResponse(str(DRFO.cleaned_data))
        

    return render(request,'registration.html',d)