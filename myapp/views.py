from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Event
from .forms import EventForm
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method=="POST":
        fm=EventForm(request.POST , request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request , 'Event Added Successfully')
            return HttpResponseRedirect('/')
    else:
        fm=EventForm()
    events = Event.objects.all()
    return render(request  , 'myapp/home.html' , {'form':fm , 'events':events})

def liked_true(request , id):
    event = Event.objects.get(pk=id)
    event.is_liked = True
    print(event.is_liked)
    event.save()
    return HttpResponseRedirect('/')