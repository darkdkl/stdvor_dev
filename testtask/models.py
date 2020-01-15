from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


def get_amount():
    if not self.id:
        self.id = int(self.objects.all().count())+1
    return sum([product.cost for product in self.products.all()])



class Product(models.Model):
    name = models.CharField(max_length=50)
    cost = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    

class Order(models.Model):
    products = models.ManyToManyField(Product, verbose_name="Продукция")
    number = models.CharField(max_length=120, blank=True,editable=False)
    date = models.DateField(auto_now=True)
    contact = models.ForeignKey(
        "Сontact", verbose_name="Контакт", on_delete=models.CASCADE)
    amount = models.FloatField(blank=True,null=True,)
    

            
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def save(self, *args, **kwargs):
        now = timezone.now()
        order = Order.objects.filter(date=now).count()
        self.number = f'{now} {int(order)+1}'

        super().save(*args, **kwargs)
        

    def __str__(self):
        return f'Заказ {self.number}'


class Сontact(models.Model):
    client = models.ForeignKey(User, verbose_name="Клиент", on_delete=models.CASCADE)
    tel_number = PhoneNumberField()
    address = models.TextField(max_length=200)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
