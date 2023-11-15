from django.db import models
from django.contrib.auth.models import User
from datetime import date
from tinymce.models import HTMLField

# Create your models here.
class Paslaugos(models.Model):
    name = models.CharField("Pavadinimas", max_length=100)
    price = models.IntegerField("Kaina €")

    class Meta:
        verbose_name = "Paslauga"
        verbose_name_plural = 'Paslaugos'

    def __str__(self):
        return f"{self.name} {self.price}"

class UzsakymoEilute(models.Model):
    service_id = models.ForeignKey("Paslaugos", on_delete= models.SET_NULL, null = True)
    # service_id = models.ManyToManyField("Paslaugos")
    order_id = models.ForeignKey("Uzsakymas", on_delete=models.SET_NULL, null=True)
    amount = models.CharField("Kiekis", max_length=5, blank=True)

    class Meta:
        verbose_name = "Uzsakymo eilute"
        verbose_name_plural = 'Uzsakymu eilutes'

    def __str__(self):
        return f"{self.order_id} Paslaugos {self.service_id} {self.amount} "

class Uzsakymas(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField("Data", null=True,blank=True)
    car_id = models.ForeignKey("Automobilis", on_delete=models.SET_NULL,null=True)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    due_back = models.DateField('Grazinti iki', null=True, blank=True)

    UZSAKYMO_STATUS = (
        ('d', 'Laukiama detaliu'),
        ('r', 'Remontuojama'),
        ('a', 'Atlikta'),
        ('p', 'Priimtas uzsakymas')
    )
    status = models.CharField(max_length=1,choices=UZSAKYMO_STATUS, blank=True,default="r",help_text="Uzsakymo statusas")

    class Meta:
        verbose_name = "Uzsakymas"
        verbose_name_plural = 'Uzsakymai'

    def __str__(self):
        return f"Uzsakymo ID: {self.id} Automobilio ID: {self.car_id} Data: {self.date} "

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

class Automobilis(models.Model):
    id = models.AutoField(primary_key=True)
    number_plate = models.CharField("Valstybinis Nr.",max_length=10)
    car_model_id = models.ForeignKey("AutomobiliuModeliai", on_delete=models.SET_NULL,null=True)
    vin_code = models.CharField("VIN kodas",max_length=20,blank=True)
    cliet = models.CharField("Klientas", max_length=30, help_text="Vardas/Pavarde")
    cover = models.ImageField('Viršelis', upload_to='covers', null=True, blank=True)
    komentaras = HTMLField(blank=True)
    class Meta:
        verbose_name = "Automobilis"
        verbose_name_plural = 'Automobiliai'

    def __str__(self):
        return f"{self.id}" #f'Valstybinis Nr: {self.number_plate} VIN: {self.vin_code} Klientas: {self.cliet}

class AutomobiliuModeliai(models.Model):
    year = models.IntegerField("Metai")
    brand = models.CharField("Marke", max_length=25)
    modelis = models.CharField("Modelis", max_length=25)
    variklis = models.CharField("Variklis", max_length=10)

    class Meta:
        verbose_name = "Automobilio modelis"
        verbose_name_plural = 'Automobiliu modeliai'

    def __str__(self):
        return f'{self.brand} {self.modelis} {self.variklis} {self.year}'

