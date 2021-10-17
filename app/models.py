from django.db import models
#from . import enum
from django.utils.translation import ugettext as _

class Etichetta(models.Model):
    nome = models.CharField(max_length=255, verbose_name=_("Nome"))
    tipo = models.IntegerField(verbose_name=_("Tipo"), default=2)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = _('Etichetta')
        verbose_name_plural = _('Etichette')
    
class Persona(models.Model):
    cognome = models.CharField(max_length=255, verbose_name=_("Cognome"))
    nome = models.CharField(max_length=255, blank=True, verbose_name=_("Nome"))
    email = models.EmailField(blank=True, verbose_name=_("Email"))
    fax = models.CharField(max_length=255, blank=True, verbose_name="Fax")
    telefono1 = models.CharField(max_length=255, blank=True, verbose_name="Tel. 1")
    telefono2 = models.CharField(max_length=255, blank=True, verbose_name="Tel. 2")
    codice1 = models.CharField(max_length=255, verbose_name=_("Codice"), blank=True)
    codiceco = models.CharField(max_length=255, verbose_name=_("Cod.2"), blank=True)
    codicecs = models.CharField(max_length=255, verbose_name=_("Cod.3"), blank=True)
    etichette = models.ManyToManyField(Etichetta, blank=True, verbose_name=_("Etichette"))
    
    class Meta:
        verbose_name = _('Persona')
        verbose_name_plural = _('Persone')
