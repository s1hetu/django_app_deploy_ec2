from .views import Contact
from django.urls import path
urlpatterns = [
    path('contact/', Contact.as_view(), name='contact')
]