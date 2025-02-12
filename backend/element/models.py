from django.db import models

class Element(models.Model):
    symbol = models.CharField(max_length=3, verbose_name='元素記号')
    number = models.PositiveIntegerField(verbose_name='元素番号')
    atomic_mass = models.FloatField(verbose_name='原子量')
    period = models.PositiveIntegerField(verbose_name='周期')
    family = models.PositiveIntegerField(verbose_name='族')
    properties = models.CharField(max_length=30, verbose_name='性質')
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name='説明')
    image = models.ImageField(upload_to='element/image/', blank=True, null=True, verbose_name='画像')
    
    def __str__(self):
        return self.symbol