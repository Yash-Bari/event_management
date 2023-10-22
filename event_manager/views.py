from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Event, Feedback
from .forms import EventForm, FeedbackForm
from django.db.models import Q
import json
from django.core.serializers import serialize

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def generate_feedback_link(request, event_id):
    event = Event.objects.get(pk=event_id)
    if not event.feedback_link:
        event.feedback_link = f'/feedback/{event_id}/'
        event.save()
    return redirect('feedback_form')

def view_feedback(request, event_id):
    feedbacks = Feedback.objects.filter(event_id=event_id)
    events = Event.objects.all()
    
    for feedback in feedbacks:
        feedback.rating_percentage = feedback.rating * 10
    
    context = {
        'event': Event.objects.get(id=event_id),
        'feedbacks': feedbacks,
    }
    
    return render(request, 'view_feedback.html', context)

def feedback_form(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.event = event
            feedback.save()
            return redirect('view_feedback', event_id=event_id)
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form, 'event': event})

def search_events(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        events = Event.objects.filter(Q(event_name__icontains=query) | Q(organizer_faculty_name__icontains=query))
        event_data = serialize('json', events)
        return JsonResponse(json.loads(event_data), safe=False)

def feedback_data(request, event_id):
    feedbacks = Feedback.objects.filter(event_id=event_id)
    data = {
        "ratings": [feedback.rating for feedback in feedbacks],
    }
    return JsonResponse(data)

