from django.urls import path
from list_contratos.views import ContratoView

urlpatterns = [
    path("contrato/", ContratoView.as_view()),
]
