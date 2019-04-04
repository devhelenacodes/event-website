from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Greeting

# Create your views here.
@login_required
def index(request):
    # return HttpResponse('Hello from Python!')
	if request.user.is_authenticated:
		return render(request, "index.html")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

@login_required
def contact(request):
	if request.user.is_authenticated:
		return render(request, "contact.html")
