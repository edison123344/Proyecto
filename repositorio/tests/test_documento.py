from turtle import title
import pytest

from documento.models import Documento
@pytest.mark.django_db
def test_documento_creation():
   documento=Documento.objects.create(
      name='123'

   )
   
   assert documento.name =='123'