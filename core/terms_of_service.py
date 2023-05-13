from django.shortcuts import render

def terms_of_service(request):
    return render(request, 'TERMS_OF_USE.html', locals())