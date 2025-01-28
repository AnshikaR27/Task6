from django.urls import path
from . import views

urlpatterns = [
    ...,
    path('visa-probability/<int:application_id>/', views.visa_probability_view, name='visa_probability'),
]
