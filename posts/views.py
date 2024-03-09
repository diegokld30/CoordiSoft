from django.http import HttpResponse
from django.views.generic.base import View

class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hola mundo")
