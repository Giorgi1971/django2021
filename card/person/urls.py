from django.urls import path
from . import views


app_name = 'person'

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', views.persons, name='persons'),
    path('add_person/', views.add_person, name='add_person'),
]
