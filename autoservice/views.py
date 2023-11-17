from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Paslaugos, Automobilis, Uzsakymas, AutomobiliuModeliai
from .forms import UzsakymasReviewForm, UserUpdateForm, ProfilisUpdateForm
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views.generic.edit import FormMixin
import re
from django.contrib.auth.decorators import login_required

"""paslaugų kiekis, atliktų užsakymų kiekis, automobilių kiekis"""
def index(request):
    paslaugu_kiekis = Paslaugos.objects.all().count()
    atliktu_uzsakymu_kiekis = Uzsakymas.objects.filter(status__exact='a').count()
    automobiliu_kiekis = Automobilis.objects.all().count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        "paslaugu_kiekis": paslaugu_kiekis,
        "atliktu_uzsakymu_kiekis": atliktu_uzsakymu_kiekis,
        "automobiliu_kiekis": automobiliu_kiekis,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)

def automobiliai(request):
    paginator = Paginator(Automobilis.objects.all(),4)
    page_number = request.GET.get("page")
    automobiliai = paginator.get_page(page_number)
    context = {
        "automobiliai": automobiliai
    }
    return render(request, "automobiliai.html", context=context)

def automobilis(request,automobilis_id):
    one_car = get_object_or_404(Automobilis, pk=automobilis_id)
    return render(request, "automobilis.html", {"automobilis": one_car})

def search(request):
    """
    paprasta paieška. query ima informaciją iš paieškos laukelio,
    search_results prafiltruoja pagal įvestą tekstą knygų pavadinimus ir aprašymus.
    Icontains nuo contains skiriasi tuo, kad icontains ignoruoja ar raidės
    didžiosios/mažosios.
    """
    query = request.GET.get('query')
    search_results = Automobilis.objects.filter(
        Q(cliet__icontains=query) |
        Q(number_plate__icontains=query) |
        Q(vin_code__icontains=query) |
        Q(car_model_id__modelis__icontains=query) |
        Q(car_model_id__brand__icontains=query)
    )
    return render(request, 'search.html', {'automobilis': search_results,'query': query})
class UzsakymasListView(generic.ListView):
    model = Uzsakymas
    paginate_by = 2
    template_name = 'uzsakymas_list.html'

class UzsakymasDetailView(FormMixin,generic.DetailView):
    model = Uzsakymas
    template_name = 'uzsakymas_detail.html'
    form_class = UzsakymasReviewForm

    # nurodome, kur atsidursime komentaro sėkmės atveju.
    def get_success_url(self):
        return reverse('uzsakymas_detail', kwargs={'pk': self.object.id})

    # standartinis post metodo perrašymas, naudojant FormMixin, galite kopijuoti tiesiai į savo projektą.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # štai čia nurodome, kad knyga bus būtent ta, po kuria komentuojame, o vartotojas bus tas, kuris yra prisijungęs.
    def form_valid(self, form):
        form.instance.uzsakymas = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(UzsakymasDetailView, self).form_valid(form)


class UzsakymaiByCustomerListView(LoginRequiredMixin,generic.ListView):
    model = Uzsakymas
    template_name = "customer_order.html"
    paginate_by = 5

    def get_queryset(self):
        return Uzsakymas.objects.filter(customer=self.request.user)


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        def validate_password(password):
            if len(password) < 8:
                return False
            if not re.search("[a-z]", password):
                return False
            if not re.search("[A-Z]", password):
                return False
            if not re.search("[0-9]", password):
                return False
            return True

            # tikriname, ar sutampa slaptažodžiai
        if validate_password(password) == True:
            if password == password2:
                # tikriname, ar neužimtas username
                if User.objects.filter(username=username).exists():
                    messages.error(request, f'Vartotojo vardas {username} užimtas!')
                    return redirect('register')
                else:
                    # tikriname, ar nėra tokio pat email
                    if User.objects.filter(email=email).exists():
                        messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                        return redirect('register')
                    else:
                        # jeigu viskas tvarkoje, sukuriame naują vartotoją
                        User.objects.create_user(username=username, email=email, password=password)
                        messages.info(request, f'Vartotojas {username} užregistruotas!')
                        return redirect('login')
            else:
                messages.error(request, 'Slaptažodžiai nesutampa!')
                return redirect('register')
        else:
            messages.error(request, 'Slaptažodis turi but 8 simboliu, bent viena didzioji raide ir bent vienas skaicius !')
            return redirect('register')
    return render(request, 'register.html')

@login_required
def profilis(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilisUpdateForm(request.POST, request.FILES, instance=request.user.profilis)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profilis atnaujintas")
            return redirect('profilis')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfilisUpdateForm(instance=request.user.profilis)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profilis.html', context)