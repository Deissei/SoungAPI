from django.shortcuts import render

def SingInViewFunction(request):
    return render(request, 'authorization/sing_in.html', locals())


def LoginInViewFunction(request):
    return render(request, 'authorization/login_in.html', locals())
