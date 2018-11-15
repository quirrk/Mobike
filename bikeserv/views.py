from django.shortcuts import render

def inicio(request):
    return render(request,'bikeserv/inicio.html',{})

def quienessomos(request):
    return render(request,'bikeserv/quienessomos.html', {})

def arrendar(request):
    return render(request,'bikeserv/arrendar.html', {})