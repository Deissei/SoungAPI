from django.shortcuts import render

def ProfileViewFunction(request):
    return render(request, 'profile/profile.html', locals())