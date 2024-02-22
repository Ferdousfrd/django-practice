from django.shortcuts import render
from django.http import HttpResponse

tasks = ["Eat", "Gym", "Grind", "Sleep"]

# Create your views here.
def index(request):
    return render (request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html")