from django.db import models

class Reservation(models.Model):
    STATUS_PENDIENTE = 'pendiente'
    STATUS_CONFIRMADA = 'confirmada'
    STATUS_CANCELADA = 'cancelada'

    STATUS_CHOICES = [
        (STATUS_PENDIENTE, 'Pendiente'),
        (STATUS_CONFIRMADA, 'Confirmada'),
        (STATUS_CANCELADA, 'Cancelada'),
    ]

    customer_name = models.CharField("Nombre del cliente", max_length=255)
    date = models.DateTimeField("Fecha y hora")
    service = models.CharField("Servicio", max_length=255)
    status = models.CharField("Estado", max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDIENTE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer_name} - {self.date.strftime('%Y-%m-%d %H:%M')}"
