from selectable.base import ModelLookup
from selectable.registry import registry
from app.models import Etichetta
from django.utils.translation import ugettext as _

class EtichettaLookup(ModelLookup):
    model = Etichetta
    search_fields = ('nome__icontains', )

    def get_item_label(self, item):
        return "%s" % (item.nome)

    def get_item_id(self, item):
        return "%s" % item.id

registry.register(EtichettaLookup)

