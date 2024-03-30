# chatbot_project/urls.py

from django.urls import path
from .views import chatbot_view, save_user_details_view  # Import the new view function

urlpatterns = [
    path('', chatbot_view, name='chatbot_view'),
    path('save_user_details/', save_user_details_view, name='save_user_details'),  # Add the new URL pattern
]