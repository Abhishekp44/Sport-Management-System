from django import forms
from .models import Player, Team, Schedule
from django.contrib.auth.forms import AuthenticationForm

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'age', 'sport', 'medical_conditions', 'team']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Player Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Player Age'}),
            'sport': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Sport Name'}),
            'medical_conditions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Any Medical Conditions', 'rows': 3}),
            'team': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Team'}),
        }
class CoachLoginForm(AuthenticationForm):
    pass

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']

class AddTeamForm(forms.ModelForm):  
    class Meta:
        model = Team
        fields = ['name', 'coach']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Team Name'}),
            'coach': forms.Select(attrs={'class': 'form-control'}),
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['team', 'date', 'event_type', 'location']
        widgets = {
            'team': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Team'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'Select Date'}),
            'event_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Type (e.g., Practice, Match)'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Location'}),
        }

