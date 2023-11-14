from django.shortcuts import render, get_object_or_404
from .models import Paslaugos, Automobilis, Uzsakymas, AutomobiliuModeliai
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
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

class UzsakymasDetailView(generic.DetailView):
    model = Uzsakymas
    template_name = 'uzsakymas_detail.html'

