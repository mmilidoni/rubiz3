"""rubiz3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home)
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home)
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from app.views import *

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
        url(r'^$', elenco_persone),
        url(r'^login$', userlogin),
        url(r'^logout$', userlogout),
        url(r'^lang$', form_lingua),
        url(r'^cambia_lingua/(?P<l>[a-z]+)/$', cambia_lingua),
        url(r'^i18n/', include('django.conf.urls.i18n')),

        url(r'^stampa_elenco/$', stampa_elenco),
        url(r'^stampa_rubrica/$', stampa_rubrica),
        url(r'^stampa_etichette/$', stampa_etichette),
        url(r'^form_stampa/(?P<tipo>elenco)/$', form_stampa),
        url(r'^form_stampa/(?P<tipo>rubrica)/$', form_stampa),
        url(r'^form_stampa/(?P<tipo>etichette)/$', form_stampa),

        url(r'^elenco_persone$', elenco_persone),
        url(r'^nuova_persona$', form_persona),
        url(r'^form_persona/$', form_persona),
        url(r'^form_persona/(?P<pk>\d+)/$', form_persona),
        url(r'^elimina_persona/(?P<pk>[\d]+)/$', elimina_persona),

        url(r'^elenco_etichette$', elenco_etichette),
        url(r'^nuova_etichetta$', form_etichetta),
        url(r'^form_etichetta/$', form_etichetta),
        url(r'^form_etichetta/(?P<pk>\d+)/$', form_etichetta),
        url(r'^elimina_etichetta/(?P<pk>[\d]+)/$', elimina_etichetta),
]