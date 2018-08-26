from django.shortcuts import render
import django_tables2 as tables

class CarsTable(tables.Table):
    id = tables.Column()
    name = tables.Column()

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

    return render(request, 'cars.html', {'cars': table})
