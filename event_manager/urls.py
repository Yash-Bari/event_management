from django.urls import path
from . import views

urlpatterns = [
    path('create_event/', views.create_event, name='create_event'),
    path('', views.event_list, name='event_list'),
    path('generate_feedback_link/<int:event_id>/', views.generate_feedback_link, name='generate_feedback_link'),
    path('view_feedback/<int:event_id>/', views.view_feedback, name='view_feedback'),
    path('feedback_form/<int:event_id>/', views.feedback_form, name='feedback_form'),
    path('search_events/', views.search_events, name='search_events'),
    path('feedback_data/<int:event_id>/', views.feedback_data, name='feedback_data'),
]
