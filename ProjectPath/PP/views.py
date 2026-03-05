from django.shortcuts import render
from django.shortcuts import redirect
from PP.models import projet
from PP.models import CompteEtudiant
from PP.form import CreateProject
from PP.form import CreateAccount

def project_list(request):
    P = projet.objects.all()
    return render(request, 'Admin/project_list.html',{'p':P})

def add_project(request):
    if request.method =="POST":
        form = CreateProject(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = CreateProject()
    return render(request, "Student/add_project.html", {'form' : form})

def project_details(request, project_id):
    project =  projet.objects.get(id = project_id)
    return render(request, "project_details.html", {"p" : project})

def modify_project(request,project_id):
    p = projet.objects.get(id= project_id)
    if request.method == "POST":
        form = CreateProject(request.POST, request.FILES, instance = p )
        if form.is_valid():
            p = form.save()
            return redirect("project_details",project_id)
    else:
        form = CreateProject(instance=p)
    return render(request,"Student/modify_project.html", {"form" : form})

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
    return render(request, "Student/create_account.html", {"form": form})

def user_authentification(request):
    if request.method == "POST":
        form = CreateAccount(request.POST)
        if exists(form) == []:
            user_id = CompteEtudiant.objects.get(matricule = form["matricule"].value()).id
            return redirect("home", user_id)
        
    else:
        form = CreateAccount()
    return render(request, "Student/authentification.html", {"form": form})

def exists(form):
    matcher = CompteEtudiant.objects.get(matricule = form["matricule"].value()).get_fields()
    i = 0
    unmatched_fields = []
    for fields in form.fields:
        if type(matcher[i]) == int:
            b= int(form[fields].value())
            if b != matcher[i]:
                unmatched_fields.append(fields)
        else:
            if form[fields].value() != matcher[i]:
                unmatched_fields.append(fields)
        i = i+1
    return unmatched_fields

def user_details(request, user_id):
    user = CompteEtudiant.objects.filter(id = user_id)
    return render(request, "Student/user.html", {"user": user})

def modify_user_account(request, user_id):
    user = CompteEtudiant.objects.get(id = user_id)
    if request.method == "POST":
        form = CreateAccount(request.POST, instance = user)
        if form.is_valid():
            user = form.save()
            return redirect("home", user.id)
    else:
        form = CreateAccount(instance= user)
    return render(request, "Student/modify_user_account.html", {"form": form})

def home(request,user_id):
    user = CompteEtudiant.objects.get(id = user_id)
    user_projects = user.projet_set.all()
    return render(request,"Student/home.html",{"user" : user, "user_projects": user_projects})


