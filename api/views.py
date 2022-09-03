from django.http import JsonResponse
from django.shortcuts import render
from django import views
from .models import Company


# Create your views here.

class Home_view(views.View):
    def get(self, request):
        content = {}

        return render(request, 'home.html', content)


class Company_view(views.View):
    def get(self, request):
        companies = list(Company.objects.values())
        if len(companies) > 0:
            datos = {
                'mensaje': 'exito',
                'companies': companies
            }
        else:
            datos = {
                'mensaje ': 'companies not found',
            }
        return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
