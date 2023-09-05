from django.urls import path
from persons.views import PersonView, PersonDetailView

urlpatterns = [
    path("persons/", PersonView.as_view()),
    path("persons/<int:person_id>/", PersonDetailView.as_view()),
]