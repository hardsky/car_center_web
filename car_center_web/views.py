from django.http import HttpResponseRedirect
from django.shortcuts import render
from django_tables2 import RequestConfig
from .tables import CarsTable
from .forms import CarForm, CarNewForm

def cars(request):
    data = [
        {
            'id': 1,
            'name': 'Test1'
        },
        {
            'id': 2,
            'name': 'Test2'
        },
        {
            'id': 3,
            'name': 'Test3'
        },
    ]

    table = CarsTable(data)
    RequestConfig(request).configure(table)
    return render(request, 'cars.html', {'cars': table})

def car_detail(request, id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CarForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/cars/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CarForm(initial = {'id': 1, 'name': 'Test1'})

    return render(request, 'car_detail.html',{'form': form})

def car_new(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CarNewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/cars/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CarNewForm()

    return render(request, 'car_new.html',{'form': form})

def car_delete(request, id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # process delete
        return HttpResponseRedirect('/cars/')

    return HttpResponseRedirect('/cars/')
