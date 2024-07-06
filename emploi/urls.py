from django.urls import path
from .views import home

app_name = 'emploi'

urlpatterns = [
    path('', home, name='index')
]
