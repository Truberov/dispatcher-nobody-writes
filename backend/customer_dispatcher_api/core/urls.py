from django.urls import path

from core.views import (
    TransportListView, TypesListView, CharacteristicListView, ReservationListCreatView, ReservationRetrieveUpdateView,
)


urlpatterns = [
    path('transport/', TransportListView.as_view()),
    path('transport/types/', TypesListView.as_view()),
    path('transport/characteristic/', CharacteristicListView.as_view()),
    path('reservation/', ReservationListCreatView.as_view()),
    path('reservation/<int:id>/', ReservationRetrieveUpdateView.as_view()),
]
