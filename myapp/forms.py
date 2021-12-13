from django import forms
from django.forms import widgets 
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields = ['event_name' , 'location' , 'image']
        labels={
            'event_name':'Event Name',
            'image':'Event Image',
            'location':'Event Location',
        }
        widgets={
            'event_name':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.Select(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'img-fluid img-thumbnail'}),
        }