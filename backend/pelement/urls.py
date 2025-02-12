from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('element/', include('element.urls')),
    path('player/', include('player.urls')),
    path('card/', include('card.urls')),
    path('battle/', include('battle.urls')),
]
