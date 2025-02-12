from django.db import models
from uuid import uuid4
from player.models import Player


class Battle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    state = models.CharField(max_length=20, default="preparation", verbose_name="戦闘状態")
    pure_substance_deck = models.JSONField(default=list, verbose_name="山札")
    turn = models.IntegerField(default=0, verbose_name="ターン数")
    winner = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="winner",
        blank=True,
        null=True,
        verbose_name="勝者"
    )
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")


class BattleParticipant(models.Model):
    ROLE_CHOICES = (
        ('player1', 'プレイヤー1'),
        ('player2', 'プレイヤー2'),
    )

    battle = models.ForeignKey(Battle, on_delete=models.CASCADE, related_name="participants")
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, verbose_name="役割")
    

    life = models.IntegerField(default=100, verbose_name="ライフ")
    energy = models.IntegerField(default=40, verbose_name="エネルギー")
    
    nature_hand = models.JSONField(default=list, verbose_name="自然手札")
    tool_hand = models.JSONField(default=list, verbose_name="化学道具手札")
    tool_deck_copy = models.JSONField(default=list, verbose_name="化学道具デッキ（コピー）")