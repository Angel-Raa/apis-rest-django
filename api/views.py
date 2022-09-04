import json
from django.http import JsonResponse
from django.shortcuts import render
from django import views
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Company


# Create your views here.

class Home_view(views.View):
    def get(self, request):
        content = {}

        return render(request, 'home.html', content)


class Company_view(views.View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):

        if id > 0:
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                datos = {
                    'mensaje ': 'success', 'companies': company
                }
            else:
                datos = {
                    'mensaje ': 'companies not found',
                }
            return JsonResponse(datos)

        else:
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
        js = json.loads(request.body)
        Company.objects.create(nombre=js['nombre'], website=js['website'])
        datos = {'mensaje': 'success'}
        return JsonResponse(datos)

    def put(self, request, id=0):
        js = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            company = Company.objects.get(id=id)
            company.nombre = js['nombre']
            company.website = js['website']
            company.save()
        else:
            datos = {
                'mensaje ': 'companies not found',
            }
        return JsonResponse(datos)

    def delete(self, request, id=0):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies) > 0:
            Company.objects.filter(id=id).delete()
            datos = {
                'mensaje ': 'companies not found',
            }
        else:
            datos = {
                'mensaje ': 'companies not found',
            }
        return JsonResponse(datos)


