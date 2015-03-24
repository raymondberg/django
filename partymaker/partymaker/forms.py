__author__ = 'rberg'
from django.forms import ModelForm
from partymaker.models import Neighborhood, Animal, AnimalRating

class NeighborhoodForm(ModelForm):
    class Meta:
        model = Neighborhood
        fields = ['name','zip_code']

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['first_name','last_name','email','phone','neighborhood']
