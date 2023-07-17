from django.shortcuts import render


def html_views(request):
    return render(request, 'index.html')

