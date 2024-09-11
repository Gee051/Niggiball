from django.urls import path
from .views import upcoming_predictions_view

urlpatterns = [
    path('predictions/', upcoming_predictions_view, name='predictions'),
    
]
