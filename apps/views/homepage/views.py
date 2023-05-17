from django.shortcuts import render


def HomePageViewFunction(request):
    return render(request, 'home/index.html', locals())
