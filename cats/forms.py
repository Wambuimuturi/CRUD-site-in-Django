from django.forms import ModelForm
from cats.models import Breed, Cat



# Create the form class.
class BreedForm(ModelForm):
    class Meta:
        model = Breed
        fields = '__all__'

class CatForm(ModelForm):
    class Meta:
        model = Cat
        fields = '__all__'        
