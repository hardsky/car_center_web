from django.shortcuts import render
from django_tables2 import RequestConfig
from .tables import CarsTable
from .forms import CarForm

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
    form = CarForm(initial = {'id': 1, 'name': 'Test1'})
    return render(request, 'car_detail.html',{'form': form})
