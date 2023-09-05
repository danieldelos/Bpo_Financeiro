# from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .models import Person
from django.forms import model_to_dict

class PersonView(APIView):
    def get(self, req: Request) -> Response:
        persons = Person.objects.all()
        converted_persons = []
        for person in persons:
            current_person = model_to_dict(person)
            converted_persons.append(current_person)
        return Response (converted_persons, status.HTTP_200_OK)

    def post(self, req: Request) -> Response:
        person = Person.objects.create(**req.data)  
        converted_person = model_to_dict(person)      
        return Response(converted_person, status.HTTP_201_CREATED)
    
class PersonDetailView(APIView):
    def get(self, req: Request, person_id: int) -> Response:
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({"msg": "Pessoa não encontrada"}, status.HTTP_404_NOT_FOUND)   
        converted_person = model_to_dict(person)      
        return Response(converted_person, status.HTTP_200_OK)
     
    def delete(self, req: Request, person_id: int) -> Response:
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({"msg": "Pessoa não encontrada"}, status.HTTP_404_NOT_FOUND)     
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, req: Request, person_id: int) -> Response:
        try:
            person = Person.objects.get(id=person_id)
        except Person.DoesNotExist:
            return Response({"msg": "Pessoa não encontrada"}, status.HTTP_404_NOT_FOUND)     
        for key, value in req.data.items():
            setattr(person, key, value)
        person.save()
        converted_person = model_to_dict(person)
        return Response(converted_person, status.HTTP_200_OK)
         