from django.db import models


class BaseCard(models.Model):
    type = models.CharField(max_length=10, verbose_name="カードタイプ")
    name = models.CharField(max_length=30, verbose_name="カード名")
    cost = models.IntegerField(default=1, verbose_name="コスト")
    description = models.TextField(
        max_length=200, blank=True, null=True, verbose_name="説明"
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class ElementCard(BaseCard):
    symbol = models.CharField(max_length=3, verbose_name="元素記号")
    number = models.PositiveIntegerField(verbose_name="元素番号")
    atomic_mass = models.FloatField(verbose_name="原子量")
    period = models.PositiveIntegerField(verbose_name="周期")
    family = models.PositiveIntegerField(verbose_name="族")
    properties = models.CharField(max_length=30, verbose_name="性質")
    image = models.ImageField(
        upload_to="element/image/", blank=True, null=True, verbose_name="画像"
    )

    def save(self, *args, **kwargs):
        if not self.type:
            self.type = "element"
        super().save(*args, **kwargs)


class PureSubstanceCard(BaseCard):
    atomic_mass = models.FloatField(verbose_name="原子量")
    elements = models.ManyToManyField(
        ElementCard, through="PureSubstanceElement", verbose_name="構成元素"
    )

    def save(self, *args, **kwargs):
        if not self.type:
            self.type = "PureSubstance"
        super().save(*args, **kwargs)


class PureSubstanceElement(models.Model):
    PureSubstance = models.ForeignKey(
        PureSubstanceCard,
        on_delete=models.CASCADE,
        related_name="PureSubstance_elements",
        verbose_name="複合カード",
    )
    element = models.ForeignKey(
        ElementCard,
        on_delete=models.CASCADE,
        related_name="element_PureSubstances",
        verbose_name="構成元素",
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="個数")

    def __str__(self):
        return f"{self.element.symbol}:{self.quantity}"


class ToolCard(BaseCard):
    effect = models.TextField(max_length=200, verbose_name="効果")

    def save(self, *args, **kwargs):
        if not self.type:
            self.type = "tool"
        super().save(*args, **kwargs)
