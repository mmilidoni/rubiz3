from app.models import Persona
import django_filters
from django.utils.translation import ugettext as _

class PersonaFilter(django_filters.FilterSet):
    cognome = django_filters.CharFilter(lookup_expr = 'icontains', label=_("Cognome"))
    nome = django_filters.CharFilter(lookup_expr = 'icontains', label=_("Nome"))
    telefono1 = django_filters.CharFilter(lookup_expr = 'icontains', label=_("Tel. 1"))
    telefono2 = django_filters.CharFilter(lookup_expr = 'icontains', label=_("Tel. 2"))
    fax = django_filters.CharFilter(lookup_expr = 'icontains', label=_("Fax"))
    class Meta:
        model = Persona
        fields = ['cognome', 'nome', 'telefono1', 'telefono2', 'fax']
