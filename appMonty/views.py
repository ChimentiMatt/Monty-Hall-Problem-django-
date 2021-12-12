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

def frontendpost(request):
    data = json.loads(request.body)
    print(data, '!!!!!!!!!!!!!!!!!!!!!!!!!')
    changeCorrect = data['changeCorrect']
    changedWrong = data['changedWrong']

    newData = OriginalAnswer(correct=changeCorrect, wrong=changedWrong)
    newData.save()
    return HttpResponse('ok')

def get_data(request):
    all_data = OriginalAnswer.objects.all()
    print(all_data,'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    data_list = []
    for item in all_data:
        data_list.append({
            'correct': item.correct,
            'wrong': item.wrong
        })
    return JsonResponse({'items': data_list})