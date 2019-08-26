import random

from django.db import models

# Create your models here.
from utils.investigacao.opcoes import suspeitos, armas, locais

class Investigacao(models.Model):
    suspeito = models.IntegerField('Suspeito')
    arma = models.IntegerField('Arma do crime')
    local = models.IntegerField('Local do crime')
    
    def __str__(self):
        return "{} - {} - {}".format(self.suspeito, self.arma, self.local)

    def criarCenaDoCrime(self):
        self.suspeito = random.choice(range(1, len(suspeitos) + 1))
        self.arma = random.choice(range(1, len(armas) + 1))
        self.local = random.choice(range(1, len(locais) + 1))

    class Meta:
        verbose_name = 'Investigacao'
        verbose_name_plural = 'Investigacoes'