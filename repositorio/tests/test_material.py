from turtle import title
import pytest
from material.models import Material
@pytest.mark.django_db
def test_material_creation():
   material=Material.objects.create(
      title='django'

   )
   
   assert material.title=='django'