"""
URL configuration for ProjectPath project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from PP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project_list/', views.project_list, name = "project_list"),
    path('add_project/', views.add_project, name = "add_project"),
    path("project_details/<int:project_id>", views.project_details, name="project_details"),
    path("project_details/update/<int:project_id>", views.modify_project, name="modify_Project"),
    #path('buisness_list/', views.buisness_list, name = "buisness_list"),
    #path('add_buisness/', views.add_ask_buisness, name="add_buisness"),
    path("confirmation/", views.confirmation, name="confirmation"),
    path("create_account/", views.create_acount, name="create_account"),
    path("home/<int:user_id>", views.home, name= "home"),
 
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
