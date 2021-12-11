from django.shortcuts import redirect, render
from .models import OriginalAnswer
from django.http import HttpResponseRedirect, HttpResponse, request, JsonResponse
import json

def myview(request):
    original = OriginalAnswer.objects.all()

    context = {
        'original': original
    }

    return render(request, 'appMonty/home.html', context)


# def postview(request):

#     originalCorrect = request.POST.get('correct')
#     originalWrong = request.POST.get('wrong')

#     OriginalAnswer.objects.create(
#         correct=originalCorrect,
#         wrong=originalWrong
#     )
#     return redirect('appMonty:myview')

def fontendpost(request):
    data = json.load(request.body)
    changeCorrect = data['changeCorrect']
    changedWrong = data['changedWrong']

    newData = OriginalAnswer(correct=changeCorrect, wrong=changedWrong)
    newData.save()
    return HttpResponse('ok')

