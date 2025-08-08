from pyexpat import model
import re
from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название') 

    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True,verbose_name='URL')

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название') 
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True,verbose_name='URL')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', verbose_name='Изображение', blank=True, null=True)
    price = models.DecimalField(default = 0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default = 0.00, max_digits=7, decimal_places=2, verbose_name='Скидка')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    
    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} Количество {self.quantity}'

    def display_id(self):
        return f'{self.id:05}'

    def sell_price(self):
        if self.discount:
            return round(self.price - (self.price * self.discount / 100), 2)
        
        return self.price