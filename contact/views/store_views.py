from django.shortcuts import render

def store(request):
    return render(request,'contact/store.html')