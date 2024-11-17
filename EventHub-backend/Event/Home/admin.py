from django.contrib import admin
# Registre os modelos no painel administrativo do Django
from .models import *

# Registrando os modelos para serem gerenciados no admin do Django
admin.site.register(Event)  # Modelo de eventos
admin.site.register(Booking)  # Modelo de reservas
admin.site.register(Venue)  # Modelo de locais
admin.site.register(Ticket)  # Modelo de ingressos
admin.site.register(TicketOption)  # Modelo de opções de ingressos
