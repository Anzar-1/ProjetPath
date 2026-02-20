from django.db import models


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
