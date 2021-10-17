from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from app.models import Persona, Etichetta
from app.tables import PersonaTable, EtichettaTable
from app.forms import PersonaForm, EtichettaForm
from app.filters import PersonaFilter
from django.contrib import messages
from django_tables2   import RequestConfig
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.util import render_html_download_pdf
from django.utils.translation import ugettext as _
from django.template import RequestContext
from django.utils import translation

def userlogin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/elenco_persone')

		messages.add_message(request, messages.ERROR, _('Login fallito.'))
		return render(request, 'login.html', {})
	elif not request.user.is_authenticated:
		messages.add_message(request, messages.INFO, _('Effettua il login.'))
		return render(request, 'login.html', {})
	else: 
		return HttpResponseRedirect('/elenco_persone')

@login_required
def userlogout(request):
	logout(request)
	return render(request, 'login.html', {})


@login_required
def elenco_persone(request):
	f = PersonaFilter(request.GET, queryset=Persona.objects.order_by("cognome"))
	table = PersonaTable(f.qs)
	RequestConfig(request).configure(table)
	return render(request, 'elenco_persone.html', {'filter': f, 'table': table})

@login_required
def form_persona(request, pk = None):
	if request.method == 'POST':
		if pk:
			obj = get_object_or_404(Persona, pk=pk)
		else:
			obj = Persona()
		form = PersonaForm(request.POST, instance=obj)
		if form.is_valid():
			if form.save():
				messages.add_message(request, messages.INFO, _('Anagrafica salvata con successo.'))
				return HttpResponseRedirect('/elenco_persone')
			else:
				messages.add_message(request, messages.ERROR, _("Errore nel salvataggio dell'anagrafica. Impossibile salvare."))
				return HttpResponseRedirect('/elenco_persone')
		else:
			messages.add_message(request, messages.ERROR, _("Errore nel salvataggio dell'anagrafica. Campi non validi."))
			return render(request, "form_persona.html", {"form": form, "pk":pk})
	else:
		if pk:
			obj = Persona.objects.get(pk=pk)
			form = PersonaForm(instance=obj)
		else:
			form = PersonaForm()
		return render(request, "form_persona.html", {"form": form, "pk":pk})

@login_required
def elimina_persona(request, pk = None):
	if pk:
		obj = get_object_or_404(Persona, pk=pk)
		obj.delete()
		messages.add_message(request, messages.INFO, _("Anagrafica eliminata con successo"))
		return HttpResponseRedirect('/elenco_persone')

@login_required
def elenco_etichette(request):
	table = EtichettaTable(Etichetta.objects.all())
	RequestConfig(request).configure(table)
	return render(request, 'elenco_etichette.html', {'table': table})

@login_required
def form_etichetta(request, pk = None):
	if request.method == 'POST':
		if pk:
			obj = get_object_or_404(Etichetta, pk=pk)
		else:
			obj = Etichetta()
		form = EtichettaForm(request.POST, instance=obj)
		if form.is_valid():
			if form.save():
				messages.add_message(request, messages.INFO, _('Etichetta salvata con successo.'))
				return HttpResponseRedirect('/elenco_etichette')

		messages.add_message(request, messages.ERROR, _("Errore nel salvataggio dell'etichetta."))
		return render(request, "form_etichetta.html", {"form": form, "pk":pk})
	else:
		if pk:
			obj = Etichetta.objects.get(pk=pk)
			form = EtichettaForm(instance=obj)
		else:
			form = EtichettaForm()
		return render(request, "form_etichetta.html", {"form": form, "pk":pk})

@login_required
def elimina_etichetta(request, pk = None):
	if pk:
		obj = get_object_or_404(Etichetta, pk=pk)
		obj.delete()
		messages.add_message(request, messages.INFO, _("etichetta eliminata con successo"))
		return HttpResponseRedirect('/elenco_etichette')

@login_required
def form_stampa(request, tipo):
	return render(request, "form_stampa.html", {"etichette": Etichetta.objects.order_by("nome"), "tipo":tipo})

@login_required
def stampa_rubrica(request):
	template='pdf_rubrica.html'
	lista = Persona.objects.order_by("cognome", "nome")
	context = {
		'list': lista
		}
	return render_html_download_pdf(request=request, template=template, context=context)

@login_required
def stampa_elenco(request):
	if request.POST:
		# non sicuro si intentazione
		template='pdf_elenco.html'
		titolo = request.POST.get('titolo')
		etichette_filter = request.POST.getlist('etichette')
		q_list = Q()
		et = []
		for e in etichette_filter:
			et.append(Etichetta.objects.get(pk=e))
			q_list.add(Q(etichette=e), Q.OR)

		lista = Persona.objects.filter(q_list).order_by("cognome", "nome")
		context= {
			'list': lista,
			'titolo': titolo,
			'etichette': et,
			}
		return render_html_download_pdf(request=request, template=template, context=context)

@login_required
def stampa_etichette(request):
	if request.POST:
		# non sicuro si intentazione
		template='pdf_etichette.html'
		titolo = request.POST.get('titolo')
		etichette_filter = request.POST.getlist('etichette')
		q_list = Q()
		et = []
		for e in etichette_filter:
			et.append(Etichetta.objects.get(pk=e))
			q_list.add(Q(etichette=e), Q.OR)

		lista = Persona.objects.filter(q_list).order_by("cognome", "nome")
		context= {
			'list': lista,
			'titolo': titolo,
			'etichette': et,
			}
		return render_html_download_pdf(request=request, template=template, context=context, margin="-T 4 -B 4 -L 4 -R 4")


def form_lingua(request):
	return render(request, 'lang.html', {
	'available_languages': ['en', 'it'],
		}, RequestContext(request))

#    return render(request, "lang.html", {'available_languages': ['en', 'it']})


def cambia_lingua(request, l):
	translation.activate(l)
	request.session[translation.LANGUAGE_SESSION_KEY] = l
	return HttpResponseRedirect('/')
