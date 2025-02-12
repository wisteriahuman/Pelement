from django.urls import path
from .views import ElementView, ElementDetailView


urlpatterns = [
    path("", ElementView.as_view(), name="elements"),
    path("<int:number>/", ElementDetailView.as_view(), name="element-detail")
]