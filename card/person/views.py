from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'person/index.html')


def persons(request):
    return render(request, 'person/person_list.html')
