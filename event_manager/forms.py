from django import forms
from .models import Event, Feedback

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_description', 'event_date', 'organizer_faculty_name']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'rating', 'suggestions']
