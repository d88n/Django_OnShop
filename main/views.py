from django.http import HttpResponse
from django.shortcuts import render

import main

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'Main page of the Online shop',
        'list': ['First', 'Second', 'Third'],
        'dict': {'first': 1, 'second': 2, 'third': 3},
        'boolean': True,
    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page') 