from django.urls import path
from .views import AllCardView, ElementCardView, PureSubstanceCardView, ToolCardView

urlpatterns = [
    path("", AllCardView.as_view(), name="all-cards"),
    path("element/", ElementCardView.as_view(), name="element-cards"),
    path("PureSubstance/", PureSubstanceCardView.as_view(), name="PureSubstance-cards"),
    path("tool/", ToolCardView.as_view(), name="tool-cards"),
]
