from django.urls import path

from api.views import Home_view, Company_view

app_name = 'api'
urlpatterns = [
    path('', Home_view.as_view(), name='home'),
    path('company/', Company_view.as_view(), name='company'),
]
