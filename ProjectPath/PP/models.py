from django.db import models

class CompteEtudiant(models.Model):
    matricule = models.fields.IntegerField()
    nom = models.fields.CharField(max_length = 100)
    prenom = models.fields.CharField(max_length = 100)
    mot_de_passe = models.fields.CharField( max_length = 100 ) #Y a surement un moyen de la rendre invisible au formulaire, jsp si c'est mon boulot pour l'instant.
    adresse_mail = models.fields.EmailField()
    telephone = models.fields.IntegerField()

    def get_fields(self):
        return([self.matricule, self.nom, self.prenom, self.mot_de_passe, self.adresse_mail, self.telephone])

class CompteAdmin(models.Model):
    nom = models.fields.CharField(max_length = 100)
    prenom = models.fields.CharField(max_length= 100)
    mot_de_passe = models.fields.CharField()
    adresse_mail = models.fields.EmailField()
    telephone = models.fields.IntegerField()

class Statut(models.TextChoices):
    NON_VUE = "NonVue"
    EN_ATTENTE = "EnAttente"
    ACCEPTE = "Accepte"
    REFUSE = "Refuse"
    DOCUMENT_MAQUANT = "DocumentManquant"

class Besoin(models.Model):
    typeDeBesoin = models.fields.CharField(max_length = 100) #si ça se trouve tu dois choisir parmi une liste
    description = models.fields.CharField(max_length = 1000)
    participants = models.ManyToManyField(CompteEtudiant)
    statut = models.fields.CharField(max_length = 16, choices = Statut.choices, default = "NonVue")

class projet(models.Model):
    nom_projet= models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    participants = models.ManyToManyField(CompteEtudiant)
    #Pour les participants niveaux formulaire, je pense ça serait mieux de faire genre.. premièrement un choix multiple
    #du genre tu écrit le nom de l'étudiant dans la barre de rechercher et ça te l'affiche, ou sa matricule jsp
    #puis que le formulaire soit dynamique, donc que tu puisse ajouter ou enlever des participant selon ce que t'ai besoin.
    #Je vais le faire après, j'ai chercher, j'ai eu la flemme de chercher a l'implementer pour l'instant.
    file_path = models.FileField(upload_to="files/", null = False,verbose_name="")
    statut = models.fields.CharField(max_length = 16, choices = Statut.choices, default = "NonVue")