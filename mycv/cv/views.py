from django.shortcuts import render

def cv_list(request):
    return render(request, 'cv/cv_list.html', {})
