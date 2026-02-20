from django.shortcuts import render
from django.shortcuts import redirect
from PP.models import projet
from PP.models import buisness
from PP.form import CreateProject
from PP.form import AskBuisness

def project_list(request):
    P = projet.objects.all()
    return render(request, 'project_list.html',{'p':P})

def buisness_list(request):
    B = buisness.objects.all()
    return render(request,'buisness_list.html',{'b': B})

def add_project(request):
    if request.method =="POST":
        form = CreateProject(request.POST)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = CreateProject()
    return render(request, "add_project.html", {'form' : form})

def add_ask_buisness(request):
    if request.method == 'POST':
        form = AskBuisness(request.POST)
        if form.is_valid():
            form.save()
            return redirect("confirmation")
    else:
        form = AskBuisness()
    return render(request, "add_buisness.html", {"form": form})

def confirmation(request):
    return render(request, "confirmation.html")