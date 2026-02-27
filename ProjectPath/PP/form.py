from django import forms
from PP.models import projet
<<<<<<< HEAD
#from PP.models import buisness
from PP.models import CompteEtudiant
=======
from PP.models import buisness
>>>>>>> 722ffde8fe751ef6ad6f4478fa46d35e5a0d0d31

class CreateProject(forms.ModelForm):
    class Meta:
        model = projet
<<<<<<< HEAD
        fields = ["nom_projet", "description", "file_path","participants"]  
    

#class AskBuisness(forms.ModelForm):
#    class Meta:
#        model = buisness
#        fields = '__all__'

class CreateAccount(forms.ModelForm):
    class Meta:
        model = CompteEtudiant
=======
        fields = '__all__'

class AskBuisness(forms.ModelForm):
    class Meta:
        model = buisness
>>>>>>> 722ffde8fe751ef6ad6f4478fa46d35e5a0d0d31
        fields = '__all__'