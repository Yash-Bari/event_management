from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_description = models.TextField()
    event_date = models.DateField()
    organizer_faculty_name = models.CharField(max_length=255)
    feedback_link = models.CharField(max_length=255)  # Ensure this field is present


class Feedback(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    rating = models.PositiveIntegerField()
    suggestions = models.TextField()
