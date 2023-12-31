from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('automobiliai/', views.automobiliai, name='automobiliai'),
    path('automobiliai/<int:automobilis_id>', views.automobilis, name='automobilis'),
    path('uzsakymai/', views.UzsakymasListView.as_view(), name='uzsakymai'),
    path('uzsakymai/<int:pk>', views.UzsakymasDetailView.as_view(), name='uzsakymas_detail'),
    path('search/', views.search, name='search'),
    path('manouzsakymai/', views.UzsakymaiByCustomerListView.as_view(), name='customer_order'),
    path('register/', views.register, name='register'),
    path('profilis/', views.profilis, name='profilis'),
    path('manouzsakymai/<int:pk>', views.UzsakymasByCustomerDetailView.as_view(), name="mano_uzsakymas"),
    path("manouzsakymai/new", views.UzsakymasByCustomerCreateView.as_view(), name="mano_uzsakymas_new"),
    path("manouzsakymai/<int:pk>/update", views.UzsakymasByCustomerUpdateView.as_view(), name="mano_uzsakymas_update"),
    path("manouzsakymai/<int:pk>/delete", views.UzsakymasByCustomerDeleteView.as_view(), name="mano_uzsakymas_delete"),
    path('i18n/', include('django.conf.urls.i18n')),
]