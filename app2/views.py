from django.shortcuts import render
from django.views import View


# Create your views here.
class Contact(View):
    def get(self, request):
        return render(request, 'app2/contact.html', {"email": "ac@gmail.com"})