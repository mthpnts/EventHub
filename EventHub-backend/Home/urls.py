from . import views
from django.urls import path

# Definição das rotas da aplicação
urlpatterns = [
    path("", views.EventListView.as_view(), name="home"),  # Página inicial
    path("events/", views.EventListView.as_view(), name="events"),  # Lista de eventos
    path("booking/", views.booking, name="booking"),  # Página para realizar reservas
    path("events/<slug:slug>/", views.EventDetailView.as_view(), name="event-detail"),  # Detalhes de um evento específico
    path("ajax/interested/", views.interested, name="interested"),  # Rota para marcar interesse via AJAX
    path("ajax/calculateTotal/", views.calculateTotal, name="total"),  # Rota para calcular o total via AJAX
    path("api/events/", views.EventListCreate.as_view(), name="events-api"),  # API para listar e criar eventos
]
