from django.urls import path
from .views import BattleView, BattleDetailView, BattleParticipantView, BattleParticipantDetailView, MatchmakingView


urlpatterns = [
    path("", BattleView.as_view(), name="battles"),
    path("<uuid:id>/", BattleDetailView.as_view(), name="battle-detail"),
    path("participant/", BattleParticipantView.as_view(), name="battle-participants"),
    path("participant/<uuid:id>/", BattleParticipantDetailView.as_view(), name="battle-participant-detail"),
    path("matchmaking/", MatchmakingView.as_view(), name="matchmaking"),
]