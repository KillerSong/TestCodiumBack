from re import template
from django.shortcuts import render
from .models import people
from django.http import HttpResponse , HttpResponseRedirect
from django.template import loader
from django.urls import reverse


# Create your views here.
def createform(request):
    peoples = people.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        "people" : peoples
    }
    return HttpResponse(template.render(context,request))


def addBlog(request):
    peoplename = request.POST['name']
    old = request.POST['age']
    phonenumber = request.POST['phone']
    member = people( name = peoplename , age = old , phone = phonenumber)
    member.save()
    return HttpResponseRedirect(reverse('Home'))
 


def delete(request,id):
    member = people.objects.get(id = id)
    member.delete()
    return HttpResponseRedirect(reverse('Home'))


def update(request , id):
    mymember =  people.objects.get(id = id)
    template =  loader.get_template('update.html')
    context = {
        'mymember' : mymember
    }
    return HttpResponse(template.render(context , request))

def addupdate(request , id ):
    name = request.POST['name']
    age = request.POST['age']
    phone = request.POST['phone']
    member = people.objects.get(id = id)
    member.name = name
    member.age = age
    member.phone = phone
    member.save()

    return HttpResponseRedirect(reverse('Home'))

