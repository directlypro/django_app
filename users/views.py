from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Users

def users(request):
    myusers = Users.objects.all().values()
    template = loader.get_template('all_users.html')
    context = {
        'myusers' : myusers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    myuser = Users.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myuser' : myuser,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Grapes'],
    }
    return HttpResponse(template.render(context, request))