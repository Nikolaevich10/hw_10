from django.db import models


class City(models.Model):
    cities = models.CharField(max_length=30, verbose_name='city')

    def __str__(self):
        return f'{self.cities}'


class Provider(models.Model):
    provider_name = models.CharField(max_length=20, verbose_name='provider')
    city = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.provider_name}'


class Product(models.Model):
    name = models.CharField(unique=True, max_length=250)
    price = models.DecimalField(max_digits=20, decimal_places=1)
    provider = models.ForeignKey(Provider, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return f'{self.name}'


class Client(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='first name', default='Client')
    last_name = models.CharField(max_length=20, verbose_name='last name')
    product = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.last_name}'
