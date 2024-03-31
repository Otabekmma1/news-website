from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name='brend')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brandlar"

class Colour(models.Model):
    name = models.CharField(max_length=50, verbose_name='Rangi')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Rang"
        verbose_name_plural = "Ranglar"

class Car(models.Model):
    model = models.CharField(max_length=100, verbose_name='rusumi')
    colour = models.ForeignKey(Colour, on_delete=models.CASCADE, verbose_name='rangi')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='brend')
    USD = '$'
    the_price = (
        (USD, '$'),
    )
    price = models.IntegerField(verbose_name='Narxi')
    price_types = models.CharField(max_length=10, verbose_name="Valyuta", choices=the_price, default='$')


    def __str__(self):
        return self.model

    class Meta:
        verbose_name = "Mashina"
        verbose_name_plural = "Mashinalar"