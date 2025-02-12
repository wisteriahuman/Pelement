from django.urls import path
from .views import PlayerView, PlayerDetailView


urlpatterns = [
    path("", PlayerView.as_view(), name="players"),
    path("<uuid:id>/", PlayerDetailView.as_view(), name="player-detail")
]