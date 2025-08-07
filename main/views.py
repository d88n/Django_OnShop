from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


import main

# Create your views here.
def index(request):
    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная страница',
        'content': 'Магазин мебели HOME',
        'categories': categories,
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'About - О нас',
        'content': 'Информация о магазине HOME',
        'text_on_page': 'Мы - команда профессионалов, специализирующихся на продаже качественной мебели. Наша цель - предоставить клиентам широкий выбор стильной и функциональной мебели для дома и офиса. Мы гордимся тем, что предлагаем только проверенные бренды и высококачественные материалы. Наша команда всегда готова помочь вам выбрать идеальные решения для вашего интерьера. Спасибо, что выбрали нас!',
        }
    
    return render(request, 'main/about.html', context)