from django.shortcuts import render

def terms_of_service(request):
    return render(request, 'docs/TERMS_OF_USE.html', locals())