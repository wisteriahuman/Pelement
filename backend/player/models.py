from django.db import models
from uuid import uuid4

class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=20, verbose_name="プレイヤー名")
    tool_deck = models.JSONField(default=list, verbose_name="化学道具カードデッキ")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")