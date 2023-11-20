from .models import UzsakymasReview, Profilis, Uzsakymas, UzsakymoEilute
from django import forms
from django.contrib.auth.models import User


class UzsakymasReviewForm(forms.ModelForm):
    class Meta:
        model = UzsakymasReview
        fields = ('content', 'uzsakymas', 'reviewer',)
        widgets = {'uzsakymas': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfilisUpdateForm(forms.ModelForm):
    class Meta:
        model = Profilis
        fields = ['nuotrauka']

class DateInput(forms.DateInput):
    input_type = 'date'

class CustomerOrderCreateForm(forms.ModelForm):
    class Meta:
        model = Uzsakymas
        fields = ["car_id","customer","due_back"]
        widgets = {"customer":forms.HiddenInput(), "due_back":DateInput()}

class CustomerOrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Uzsakymas
        fields = ["car_id","customer","due_back"]
        widgets = {"customer": forms.HiddenInput(), "car_id": forms.HiddenInput(), "due_back": DateInput()}



