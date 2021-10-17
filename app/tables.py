import django_tables2 as tables
from app.models import Persona, Etichetta
from django_tables2_simplefilter import F
from django.utils.translation import ugettext as _

TEMPLATE = '<a href="%s/{{record.pk}}">'+ _("Modifica") + '</a> <a onclick="return confermaEliminazione();" href="%s/{{record.pk}}">'+_("Elimina")+ '</a>'

class PersonaTable(tables.Table):
    column_name = tables.TemplateColumn(TEMPLATE % ('form_persona', 'elimina_persona'), verbose_name=_("Azioni"))

    class Meta:
        model = Persona
        attrs = {"class": "paleblue"}
        exclude = ("id","codicecs", "codiceco")

    filters = (F('cognome','Cognome',values_list=[ (str(x), x.cognome) for x in Persona.objects.all()]))


class EtichettaTable(tables.Table):
    column_name = tables.TemplateColumn(TEMPLATE % ('form_etichetta', 'elimina_etichetta'), verbose_name=_("Azioni"))
    
    class Meta:
        model = Etichetta
        attrs = {"class": "paleblue"}
        exclude = ("id","tipo")
