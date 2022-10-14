from django.urls import path

from core.views import TransportListView


urlpatterns = [
    path('transport/', TransportListView.as_view()),

]
