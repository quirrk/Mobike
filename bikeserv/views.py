from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request,'bikeserv/inicio.html',{})

def quienessomos(request):
    return render(request,'bikeserv/quienessomos.html', {})

@login_required
def arrendar(request):
    return render(request,'bikeserv/arrendar.html', {})

