from django import forms
from .models import RestaurantLocations
from .validators import validate_category

class RestaurantsCreateForm(forms.Form):
    name      = forms.CharField()
    location  = forms.CharField(required=False)
    category  = forms.CharField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get("name")


class RestaurantLocationsCreateForm(forms.ModelForm):
    category = forms.CharField(required=False, validators=[validate_category])
    class Meta:
        model  = RestaurantLocations
        fields = [
            'name',
            'location',
            'category',
        ]

