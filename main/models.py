from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Pedido (models.Model): 
    descricao = models.CharField(max_length=200)
    data = models.DateTimeField() 