#----- urls.py -----
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('automobiliai/', views.automobiliai, name='automobiliai'),
    path('uzsakymai/', views.uzsakymai, name='uzsakymai'),
    path('kainynas/', views.kainynas, name='kainynas'),
    path('klientai/', views.klientai, name='klientai'),
    path('uzsakymai/<int:uzsakymas_id>', views.uzsakymas, name='uzsakymas'),
    path('automobiliai/<int:automobilis_id>', views.automobilis, name='automobilis'),
]

#----- models.py -----

from django.db import models
# Create your models here.

class AutomobilioModelis(models.Model):
    # automobilio modelis
    marke = models.CharField('Automobilio markė', max_length=40, null=False, help_text='Įveskite automobilio markę')
    modelis = models.CharField('Automobilio modelis', max_length=40, null=False,
                               help_text='Įveskite automobilio markės modelį')
    class Meta:
        verbose_name = 'Automobilio modelis'
        verbose_name_plural = 'Automobilių modeliai'
    def __str__(self):
        return f'{self.marke} {self.modelis}'

class Automobilis(models.Model):
    # automobilis pagal modeli ir valst.nr+vin+klientas
    valstybinis_nr = models.CharField('Automobilio valstybinis Nr.',
                                      max_length=7, null=False, unique=True, help_text='Įveskite valstybinį numerį')
    automobilio_modelis_id = models.ForeignKey('AutomobilioModelis', verbose_name='Automobilio modelis',
                                               on_delete=models.CASCADE, null=False)
    vin_kodas = models.CharField(max_length=17, null=False, unique=True, help_text='Įveskite automobilio VIN kodą')
    klientas = models.CharField(max_length=100, null=False,
                                help_text='Iveskite klientą (įmonės pavadinimas arba vardas/pavardė)')
    class Meta:
        verbose_name = 'Automobilis'
        verbose_name_plural = 'Automobiliai'
    def __str__(self):
        return f'{self.valstybinis_nr}, {self.automobilio_modelis_id}, {self.klientas}'

class Uzsakymas(models.Model):
    # uzsakymas kuriame gali buti daug uzsakymo eiluciu
    data = models.DateField('Užsakymo data', null=False)
    automobilis_id = models.ForeignKey('Automobilis', verbose_name='Informacija', on_delete=models.CASCADE, null=False)
    UZSAKYMO_STATUSAS = (
        ('l', 'Laukiama automobilio'),
        ('a', 'Automobilis tvarkomas'),
        ('u', 'Užsakymas atliktas'),
        ('x', 'Užsakymas atšauktas'),
    )
    statusas = models.CharField(max_length=1, choices=UZSAKYMO_STATUSAS, default='l', null=False, help_text='Statusas')
    class Meta:
        verbose_name = 'Užsakymas'
        verbose_name_plural = 'Užsakymai'
    def __str__(self):
        return f'{self.data}: {self.automobilis_id}'
    def is_viso(self):
        # suskaiciuoju visu eiluciu uzsakymu suma
        self.suma = 0
        for eilute in self.uzsakymoeilute_set.all():
            self.suma += eilute.viso_eilute()
        return self.suma

class UzsakymoEilute(models.Model):
    # viena eilute viena paslauga
    paslauga_id = models.ForeignKey('Paslauga', verbose_name='Paslauga', on_delete=models.CASCADE, null=False)
    uzsakymas_id = models.ForeignKey('Uzsakymas', verbose_name='Užsakymo informacija', on_delete=models.CASCADE,
                                     null=False)
    kiekis = models.IntegerField(null=False, help_text="Įveskite kiekį")
    class Meta:
        verbose_name = 'Užsakymo eilutė'
        verbose_name_plural = 'Užsakymo eilutės'
    def __str__(self):
        return f'{self.paslauga_id} - {self.uzsakymas_id} - {self.kiekis} vnt.'
    def viso_eilute(self):
        # suskaiciuoju eilutes suma
        return self.kiekis * self.paslauga_id.kaina

class Paslauga(models.Model):
    # paslaugos pavadinimas ir kaina
    pavadinimas = models.CharField('Paslaugos pavadinimas', max_length=200, null=False, unique=True,
                                   help_text='Įveskite paslaugos pavadinimą')
    kaina = models.FloatField('Kaina', max_length=10, null=False, help_text='Įveskite paslaugos kainą')
    class Meta:
        verbose_name = 'Paslauga'
        verbose_name_plural = 'Paslaugos'
    def __str__(self):
        return f'{self.pavadinimas}'

#----- views.py -----

from django.shortcuts import render, get_object_or_404
from .models import Automobilis, Uzsakymas, Paslauga
# Create your views here.

def index(request):
    paslaugu_kiekis = Paslauga.objects.all().count()
    automobiliu_kiekis = Automobilis.objects.all().count()
    klientu_kiekis = Automobilis.objects.all().count()
    uzsakymu_kiekis = Uzsakymas.objects.all().count()
    atlikti_uzsakymai = Uzsakymas.objects.all().filter(statusas__exact='u').count()
    vykdomi_uzsakymai = Uzsakymas.objects.all().filter(statusas__exact='a').count()
    laukiami_uzsakymai = Uzsakymas.objects.all().filter(statusas__exact='l').count()
    atsaukti_uzsakymai = Uzsakymas.objects.all().filter(statusas__exact='x').count()
    context = {
        'paslaugu_kiekis': paslaugu_kiekis,
        'automobiliu_kiekis': automobiliu_kiekis,
        'klientu_kiekis': klientu_kiekis,
        'uzsakymu_kiekis': uzsakymu_kiekis,
        'atlikti_uzsakymai': atlikti_uzsakymai,
        'vykdomi_uzsakymai': vykdomi_uzsakymai,
        'laukiami_uzsakymai': laukiami_uzsakymai,
        'atsaukti_uzsakymai': atsaukti_uzsakymai,
    }
    return render(request, 'index.html', context=context)

def automobiliai(request):
    visi_automobiliai = Automobilis.objects.all()
    context = {
        'visi_automobiliai': visi_automobiliai,
    }
    return render(request, 'automobiliai.html', context=context)

def kainynas(request):
    kainynas = Paslauga.objects.all()
    context = {
        'kainynas': kainynas,
    }
    return render(request, 'kainynas.html', context=context)

def uzsakymai(request):
    uzsakymai = Uzsakymas.objects.all()
    context = {
        'uzsakymai': uzsakymai,
    }
    return render(request, 'uzsakymai.html', context=context)

def klientai(request):
    klientai = Automobilis.objects.all()
    context = {
        'klientai': klientai,
    }
    return render(request, 'klientai.html', context=context)

def uzsakymas(request, uzsakymas_id):
    uzsakymas = get_object_or_404(Uzsakymas, pk=uzsakymas_id)
    context = {
        'uzsakymas': uzsakymas,
    }
    return render(request, 'uzsakymas.html', context=context)

def automobilis(request, automobilis_id):
    automobilis = get_object_or_404(Automobilis, pk=automobilis_id)
    context = {
        'automobilis': automobilis,
    }
    return render(request, 'automobilis.html', context=context)