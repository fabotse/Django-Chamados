from ast import Num
from tkinter import CASCADE
from django.db import models
import uuid

# Create your models here.
class Chamado(models.Model):
    STATUS_CHAMADO = (
        ('Solicitação', 'Solicitação'),
        ('Dúvida', 'Dúvida'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    categoria = models.ForeignKey('Categoria',null=False, blank=False, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200,choices=STATUS_CHAMADO, blank=False, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Categoria(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name