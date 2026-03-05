from django import forms
from PP.models import projet
from PP.models import Besoin
from PP.models import CompteEtudiant
from PP.models import CompteAdmin

class CreateProject(forms.ModelForm):
    class Meta:
        model = projet
        exclude =  ('statut',)

class requestNeed(forms.ModelForm):
    class Meta:
        model = Besoin
        exclude =  ('statut',)

class CreateAccount(forms.ModelForm):
    class Meta:
        model = CompteEtudiant
        fields = '__all__'

class CreateAdmin(forms.ModelForm):
    class Meta:
        model = CompteAdmin
        fields = '__all__'