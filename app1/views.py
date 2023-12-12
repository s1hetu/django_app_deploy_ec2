from django.shortcuts import render
from django.views import View


# Create your views here.
class About(View):
    def get(self, request):
        return render(request, 'app1/about.html', context={'name': "Hetvee"})