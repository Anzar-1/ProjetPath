from django.db import models

<<<<<<< HEAD
#class buisness(models.Model):
 #   nom_projet = models.fields.CharField(max_length=100)
 #   adresse_siege_social = models.fields.CharField(max_length = 200)
 #   class form_juridique(models.Choices):
 #       SARL= "SARL"
 #       EURL = "EURL"
 #   formeJuridique = models.fields.CharField(choices=form_juridique.choices)
 #   activite = models.fields.CharField(max_length=200)
 #   numero_registre_commerce = models.fields.IntegerField()
 #   #copie_registre_commerce = models.fields.FilePathField()
 #   numero_identification_fiscale = models.fields.IntegerField()

#    description = models.fields.CharField(max_length=1000)

class CompteEtudiant(models.Model):
    nom = models.fields.CharField(max_length = 100)
    prenom = models.fields.CharField(max_length = 100)
    #ça serait bien d'en faire une clé primaire.
    mot_de_passe = models.fields.CharField( max_length = 100 ) #Y a surement un moyen de la rendre invisible au formulaire, jsp si c'est mon boulot pour l'instant.
    adresse_mail = models.fields.EmailField()
    telephone = models.fields.IntegerField()

class projet(models.Model):
    nom_projet= models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    participants = models.ManyToManyField(CompteEtudiant)
    #Pour les participants niveaux formulaire, je pense ça serait mieux de faire genre.. premièrement un choix multiple
    #du genre tu écrit le nom de l'étudiant dans la barre de rechercher et ça te l'affiche, ou sa matricule jsp
    #puis que le formulaire soit dynamique, donc que tu puisse ajouter ou enlever des participant selon ce que t'ai besoin.
    #Je vais le faire après, j'ai chercher, j'ai eu la flemme de chercher a l'implementer pour l'instant.
    file_path = models.FileField(upload_to="files/", null = False,verbose_name="")
=======

class projet(models.Model):
    nom = models.fields.CharField(max_length=100)
    prenom = models.fields.CharField(max_length=100)
    nom_projet= models.fields.CharField(max_length=100)
    adresse_mail = models.fields.EmailField()
    telephone = models.fields.IntegerField()
    description = models.fields.CharField(max_length=1000)
    #je sais pas si je mets les documents separement


class buisness(models.Model):
    nom_projet = models.fields.CharField(max_length=100)
    adresse_siege_social = models.fields.CharField(max_length = 200)
    class form_juridique(models.Choices):
        SARL= "SARL"
        EURL = "EURL"
    formeJuridique = models.fields.CharField(choices=form_juridique.choices)
    activite = models.fields.CharField(max_length=200)
    numero_registre_commerce = models.fields.IntegerField()
    #copie_registre_commerce = models.fields.FilePathField()
    numero_identification_fiscale = models.fields.IntegerField()

    description = models.fields.CharField(max_length=1000)
>>>>>>> 722ffde8fe751ef6ad6f4478fa46d35e5a0d0d31
