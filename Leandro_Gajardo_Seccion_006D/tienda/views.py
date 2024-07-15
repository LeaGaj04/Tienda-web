from django.shortcuts import render,redirect

def index(request):

    return render(request, 'index.html')

def pago(request):
    return render(request, 'pago.html')