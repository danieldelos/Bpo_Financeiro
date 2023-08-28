from django.urls import path
from persons.views import PersonView

urlpatterns = [
    path("persons/", PersonView.as_view()),
]