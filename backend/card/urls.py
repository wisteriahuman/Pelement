from django.urls import path
from .views import AllCardView, ElementCardView, CompoundCardView, ToolCardView

urlpatterns = [
    path("", AllCardView.as_view(), name="all-cards"),
    path("element/", ElementCardView.as_view(), name="element-cards"),
    path("compound/", CompoundCardView.as_view(), name="compound-cards"),
    path("tool/", ToolCardView.as_view(), name="tool-cards"),
]