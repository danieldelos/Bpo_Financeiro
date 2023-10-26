from django.urls import path
from list_contratos.views import ContratoDetailView, ContratoView, UploadPlanilhaView

urlpatterns = [
    path("contrato/", ContratoView.as_view()),
    path("contrato/<int:id_contrato>/", ContratoDetailView.as_view()),
    path('contrato/upload/', UploadPlanilhaView.as_view()),
]
