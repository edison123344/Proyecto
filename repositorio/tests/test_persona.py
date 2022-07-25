from turtle import title
import pytest
from persona.models import Persona, Titulo 

@pytest.mark.django_db
def test_persona_creation():
   titulo=Titulo.objects.create(
      name='ing'
   )
   persona= Persona.objects.create(
       name='edison',
       lastname='morales',
       mail='aaa@gmail' ,
       title=titulo
  )
   
   assert persona.name=='edison'

