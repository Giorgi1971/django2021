from django.shortcuts import get_list_or_404, render
from .models import Person
# Create your views here.

def index(request):
    return render(request, 'person/index.html')


def persons(request):
    person_list = get_list_or_404(Person)
    return render(request, 'person/person_list.html', {'person_list':person_list})
