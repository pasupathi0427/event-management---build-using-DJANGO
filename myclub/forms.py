from .models import Events, Venue
from django import forms
from django.forms.widgets import SplitDateTimeWidget



class AddVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name' , 'address' ,'phone' ,'pincode','web','email' ,'image']
        widgets={

            'name':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Venue name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Venue Address '}),
            'phone':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone '}),
            'pincode':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter pincode '}),
            'web':forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter Web URL '}),
            'email':forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address '})
        }


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'event_date', 'Venue', 'manager','description','attendees']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter event name'}),
            'event_date': forms.DateTimeInput(
                attrs={'class': 'form-control', 'type': 'datetime-local', 'placeholder': 'Select date and time'}
            ),
            'Venue': forms.Select(attrs={'class': 'form-control'}),
            'manager': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter event description'}),
            'attendees': forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
        }