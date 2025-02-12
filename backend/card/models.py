from django.db import models
from element.models import Element

class BaseCard(models.Model):
    type = models.CharField(max_length=10, verbose_name='カードタイプ')
    name = models.CharField(max_length=30, verbose_name='カード名')
    cost = models.IntegerField(verbose_name='コスト')
    
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True

class ElementCard(BaseCard, Element):
    def save(self, *args, **kwargs):
        if not self.type:
            self.type = 'element'
        super().save(*args, **kwargs)

class CompoundCard(BaseCard):
    atomic_mass = models.FloatField(verbose_name='原子量')
    elements = models.ManyToManyField(ElementCard, verbose_name='構成元素')
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name='説明')
    def save(self, *args, **kwargs):
        if not self.type:
            self.type = 'compound'
        super().save(*args, **kwargs)

class ToolCard(BaseCard):
    effect = models.TextField(max_length=200, verbose_name='効果')
    description = models.TextField(max_length=200, blank=True, null=True, verbose_name='説明')
    def save(self, *args, **kwargs):
        if not self.type:
            self.type = 'tool'
        super().save(*args, **kwargs)