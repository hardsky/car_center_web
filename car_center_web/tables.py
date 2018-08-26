import django_tables2 as tables

class CarsTable(tables.Table):
    id = tables.TemplateColumn('<a href="{% url \'car_detail\' record.id %}">{{record.id}}</a>')
    name = tables.Column()
    action_column = tables.TemplateColumn(template_name='car_action_column.html')

    class Meta:
        template_name = 'django_tables2/bootstrap.html'
