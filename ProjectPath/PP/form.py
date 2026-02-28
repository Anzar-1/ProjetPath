from django import forms
from PP.models import projet
#from PP.models import buisness
from PP.models import CompteEtudiant

class CreateProject(forms.ModelForm):
    class Meta:
        model = projet
        fields = '__all__' 
    

#class AskBuisness(forms.ModelForm):
#    class Meta:
#        model = buisness
#        fields = '__all__'

class CreateAccount(forms.ModelForm):
    class Meta:
        model = CompteEtudiant
        fields = '__all__'