from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Definição dos modelos


class Venue(models.Model):
    # Modelo para locais do evento
    title = models.CharField(max_length=150)  # Nome do local
    address = models.CharField(max_length=150)  # Endereço do local
    city = models.CharField(max_length=20)  # Cidade onde o local está

    def __str__(self):
        return f'{self.title} - {self.address}, {self.city}'


class TicketOption(models.Model):
    # Modelo para opções de ingresso
    name = models.CharField(max_length=20)  # Nome da opção de ingresso
    description = models.CharField(max_length=50, null=True, blank=True)  # Descrição opcional
    price = models.DecimalField(max_digits=5, decimal_places=2)  # Preço do ingresso

    class Meta:
        ordering = ['price']  # Ordenar pelas opções mais baratas


class Event(models.Model):
    # Modelo para eventos
    title = models.CharField(max_length=50)  # Nome do evento
    slug = models.SlugField(unique=True, null=True)  # URL amigável do evento
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)  # Local do evento
    organizer = models.ManyToManyField(
        User, help_text='Adicione organizadores', related_name='organizer', blank=True, null=True
    )  # Organizadores do evento
    date = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name='Data de Início'
    )  # Data do evento
    time = models.TimeField(
        verbose_name='Hora de Início', auto_now=False
    )  # Hora de início do evento
    baseFee = models.DecimalField(max_digits=5, decimal_places=2)  # Taxa base do evento
    imagePath = models.CharField(
        max_length=30, null=True, default="Image/test.png"
    )  # Caminho para a imagem do evento
    interested = models.ManyToManyField(
        User, help_text='Quem está interessado', related_name='interested', blank=True
    )  # Usuários interessados no evento
    ticketOptions = models.ManyToManyField(
        TicketOption, related_name="options"
    )  # Opções de ingressos para o evento

    def __str__(self):
        return f'{self.title} at {self.venue}'

    def get_absolute_url(self):
        # Retorna a URL absoluta para os detalhes do evento
        return reverse('event-detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        # Gera automaticamente o slug com base no título
        self.slug = slugify(self.title)
        super(Event, self).save(*args, **kwargs)

    class Meta:
        ordering = ['date', 'time']  # Ordenação por data e hora do evento


class Booking(models.Model):
    # Modelo para reservas de ingressos
    event = models.ForeignKey(Event, on_delete=models.CASCADE)  # Evento reservado
    booker = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuário que realizou a reserva
    booked_on = models.DateField(
        auto_now=True, auto_now_add=False, verbose_name='Data da Reserva'
    )  # Data em que a reserva foi feita
    ticketNum = models.IntegerField(
        verbose_name="Quantidade de Ingressos", default=1
    )  # Número de ingressos reservados

    def __str__(self):
        return f'{self.booker} reservou {self.event} em {self.booked_on}'

    def save(self, *args, **kwargs):
        # Salva a reserva e cria os ingressos correspondentes
        super(Booking, self).save(*args, **kwargs)
        for i in range(self.ticketNum):
            Ticket.objects.create(bookingId=self)


class Ticket(models.Model):
    # Modelo para ingressos individuais
    bookingId = models.ForeignKey(Booking, on_delete=models.CASCADE)  # Reserva associada

    def __str__(self):
        return f"Reserva ID: {self.bookingId}"