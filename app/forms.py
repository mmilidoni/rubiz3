from django import forms
from app.models import Persona, Etichetta
#from app.lookups import *
#import selectable.forms as selectable
#from datetimewidget.widgets import DateTimeWidget

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class EtichettaForm(forms.ModelForm):
    class Meta:
        model = Etichetta
        fields = ['nome']
