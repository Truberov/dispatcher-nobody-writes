from django.urls import path

from core.views import (
    TransportListView, TypesListView, CharacteristicListView,
)


urlpatterns = [
    path('transport/', TransportListView.as_view()),
    path('transport/types/', TypesListView.as_view()),
    path('transport/characteristic/', CharacteristicListView.as_view()),
]
