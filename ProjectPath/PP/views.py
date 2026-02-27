from django.shortcuts import render
from django.shortcuts import redirect
from PP.models import projet
#from PP.models import buisness
from PP.models import CompteEtudiant
from PP.form import CreateProject
#from PP.form import AskBuisness
from PP.form import CreateAccount

def project_list(request):
    P = projet.objects.all()
    return render(request, 'project_list.html',{'p':P})

#def buisness_list(request):
#    B = buisness.objects.all()
#    return render(request,'buisness_list.html',{'b': B})

def add_project(request):
    if request.method =="POST":
        form = CreateProject(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = CreateProject()
    return render(request, "add_project.html", {'form' : form})

#def add_ask_buisness(request):
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

def create_acount(request):
    if request.method == "POST":
        form = CreateAccount(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("home", user.id)
    else:
        form = CreateAccount()
    return render(request, "create_account.html", {"form": form})

def home(request,user_id):
    user = CompteEtudiant.objects.get(id = user_id)
    user_projects = user.projet_set.all()
    return render(request,"home.html",{"user" : user, "user_projects": user_projects})

def project_details(request, project_id):
    project =  projet.objects.get(id = project_id)
    return render(request, "project_details.html", {"p" : project})