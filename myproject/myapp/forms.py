from django import forms
from django.forms import ModelForm

from.models import*

class Package_Form(forms.ModelForm):
    class Meta:
        model=Pakage
        fields=['location','image','price','Dates','shortdescription','fulldescription']
class Booking_Form(forms.ModelForm):
    class Meta:
        model=TravelBook
        fields=['firstname','lastname','email','phone','destination']