from django.shortcuts import render
from .models import OriginalAnswer

def myview(request):
    original = OriginalAnswer.objects.all()

    context = {
        'original': original
    }
    return render(request, 'appMonty/home.html', context)