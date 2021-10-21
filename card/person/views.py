from django import forms
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_list_or_404, render
from .models import Person
from .forms import PersonForm
# Create your views here.

def index(request):
    return render(request, 'person/index.html')


def persons(request):
    person_list = get_list_or_404(Person)
    return render(request, 'person/person_list.html', {'person_list':person_list})


def add_person(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        print(form['birth_date'])
        print(form['photo'])
        if form.is_valid():
            print('Validaded succesfully')
            print('Nammme: '+form.cleaned_data['first_name'])
            ff = form.save(commit=False)
            print(request.FILES)

            if 'photo' in request.FILES:
                ff.photo = request.FILES['photo']

            form.save(commit=True)
            return index(request)
        else:
            return HttpResponse("No valid forms")
    return render(request, 'person/add_person.html', {'form':form})
