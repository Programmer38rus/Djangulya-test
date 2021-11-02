from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from first_app.models import FirstModel


# Create your views here.
def first_model_list(request):
    template = loader.get_template('first_template.html')
    first = FirstModel.objects.all()
    list = []
    for obj in first:
        list.append(obj)

    return HttpResponse(template.render({'obj': list, 'count': first.count()}, request))