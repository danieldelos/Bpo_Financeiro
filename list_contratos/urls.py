from django.urls import path
from list_contratos.views import ContratoDetailView, ContratoView

urlpatterns = [
    path("contrato/", ContratoView.as_view()),
    path("contrato/<int:id_contrato>/", ContratoDetailView.as_view()),
]
