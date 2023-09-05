from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    
    def __repr__(self) -> str:
       return f"<{self.id} - {self.name}>"
    
     
    
