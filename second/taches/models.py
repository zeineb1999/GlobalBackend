from django.db import models
from .models import *
from django.db.models import Q
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
class ProfileUser(models.Model):
    userId = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    role = models.CharField(max_length=30, blank=True)
    def str(self):
            return str(self.userId)
    class Meta:
        db_table = 'quickstart_profile_user'
class Batiment(models.Model):
    nomBatiment = models.CharField(max_length=500)
    typeBatiment = models.CharField(max_length=500,null=True, blank=True)
    def str(self):
            return self.nomBatiment
    class Meta:
        db_table = 'quickstart_batiment'
    def calculerConsommationTotaleBatiment(self):
        etages_batiment = self.etage_set.all()
        consommation_totale_batiment = 0
        for etage in etages_batiment:
            consommation_totale_batiment += etage.calculerConsommationTotaleEtage()

        return consommation_totale_batiment

    def calculerConsommationBatimentParPeriode(self, dateDebut, dateFin):
        etages = self.etage_set.all()
        consommation = 0
        for etage in etages:
            #print(etage.calculerConsommationEtageParPeriode(dateDebut, dateFin))
            consommation += etage.calculerConsommationEtageParPeriode(dateDebut, dateFin)

        return consommation

class Etage(models.Model):
    surface= models.FloatField(null=True, blank=True)
    nomEtage= models.CharField(max_length=500, null=True, blank=True)
    batimentId = models.ForeignKey(Batiment,on_delete=models.CASCADE)
    def __str__(self):
            return self.nomEtage
    class Meta:
        db_table = 'quickstart_etage'
    def calculerConsommationTotaleEtage(self):
        zones_etage = self.zone_set.all()
        consommation_totale_etage = 0
        for zone in zones_etage:
            consommation_totale_etage += zone.calculerConsommationTotaleZone()

        return consommation_totale_etage

    def calculerConsommationEtageParPeriode(self, dateDebut, dateFin):
        locaux = self.zone_set.all()
        consommation = 0
        for local in locaux:
            #print(local.calculerConsommationLocalParPeriode(dateDebut, dateFin))
            consommation += local.calculerConsommationLocalParPeriode(dateDebut, dateFin)

        return consommation

class Zone(models.Model):
    nomLocal = models.CharField(max_length=500)
    typeLocal = models.CharField(max_length=500, null=True, blank=True)
    etageZ = models.ForeignKey(Etage, on_delete=models.CASCADE)
    surface = models.FloatField(null=True, blank=True)
    minT = models.FloatField(null=True, blank=True)
    maxT = models.FloatField(null=True, blank=True)
    minH = models.FloatField(null=True, blank=True)
    maxH = models.FloatField(null=True, blank=True)
    """ def str(self):
            return self.nomLocal """
    class Meta:
        db_table = 'quickstart_zone'
    def calculerConsommationTotaleZone(self):
        equipements_zone = self.equipement_set.all()
        consommation_totale_zone = 0
        for equipement in equipements_zone:
            consommation_totale_zone += equipement.calculerConsommationTotale()

        return consommation_totale_zone

    def calculerConsommationLocalParPeriode(self, dateDebut, dateFin):
        equipements = self.equipement_set.all()
        consommation_local = 0
        for equipement in equipements:
            #print(equipement.calculerConsommationParPeriode(dateDebut, dateFin))
            consommation_local += equipement.calculerConsommationParPeriode(dateDebut, dateFin)

        return consommation_local

class Equipement(models.Model):
    # Définition des choix pour les états et les catégories
    ETAT_CHOICES = (("ON", "ON"), ("OFF", "OFF"))
    CATEGORIE_CHOICES = (("critique", "critique"), ("normal", "normal"))

    # Définition des champs du modèle
    nom = models.CharField(max_length=500)
    etat = models.CharField(max_length=100, choices=ETAT_CHOICES, default='ON')  # Définition de la valeur par défaut pour l'état
    type = models.CharField(max_length=100)  # Définition de la valeur par défaut pour la catégorie
    categorie = models.CharField(max_length=500, null=True, blank=True)
    puissance = models.FloatField(null=True, blank=True)
    minC = models.FloatField(null=True, blank=True)
    maxC = models.FloatField(null=True, blank=True)
    
    zoneE = models.ForeignKey(Zone, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
    class Meta:
        db_table = 'quickstart_equipement'

    def calculerConsommationTotale(self):
        #periodes_activite = self.periodeactivite_set.filter(id__lt= 1000)
        periodes_activite = self.periodeactivite_set.all()
        consommation_totale = 0
        for periode in periodes_activite:

            #print (periode.id, '/ cons: ', consommation_totale, ' + ', periode.consommation, ' = ', consommation_totale + periode.consommation)
            consommation_totale = consommation_totale + periode.consommation
        return consommation_totale


    def calculerConsommationParPeriode(self, dateDebut, dateFin):

        date_debut = datetime.strptime(dateDebut, '%Y-%m-%d %H:%M:%S')
        date_fin = datetime.strptime(dateFin, '%Y-%m-%d %H:%M:%S')
        #print('date_debut: ', date_debut)

        #periodes_activite = self.periodeactivite_set.filter(id__lt= 1000)
        periodes_activite = self.periodeactivite_set.all()
        #print('periodes: ', periodes_activite)
        consommation_totale = 0
        for periode in periodes_activite:

            """ print('periode: ', periode.id, ' : ', periode.tempsDebut, ' -> ', periode.tempsFin, ' : ', (periode.tempsDebut.timestamp() <= date_debut.timestamp() and periode.tempsFin.timestamp() >= date_fin.timestamp()) or \
            (periode.tempsDebut.timestamp() >= date_debut.timestamp() and periode.tempsFin.timestamp() <= date_fin.timestamp()) or \
            (periode.tempsDebut.timestamp() <= date_debut.timestamp() and periode.tempsFin.timestamp() <= date_fin.timestamp() and periode.tempsFin.timestamp() >= date_debut.timestamp()) or \
            (periode.tempsDebut.timestamp() >= date_debut.timestamp() and periode.tempsFin.timestamp() >= date_fin.timestamp() and periode.tempsDebut.timestamp() <= date_fin.timestamp()))
             """
            if (periode.tempsFin==None):
              periode.tempsFin = datetime.now()
            if (periode.tempsDebut.timestamp() <= date_debut.timestamp() and periode.tempsFin.timestamp() >= date_fin.timestamp()) or \
            (periode.tempsDebut.timestamp() >= date_debut.timestamp() and periode.tempsFin.timestamp() <= date_fin.timestamp()) or \
            (periode.tempsDebut.timestamp() <= date_debut.timestamp() and periode.tempsFin.timestamp() <= date_fin.timestamp() and periode.tempsFin.timestamp() >= date_debut.timestamp()) or \
            (periode.tempsDebut.timestamp() >= date_debut.timestamp() and periode.tempsFin.timestamp() >= date_fin.timestamp() and periode.tempsDebut.timestamp() <= date_fin.timestamp()):

                if periode.tempsDebut.timestamp() == date_debut.timestamp() and periode.tempsFin.timestamp() == date_fin.timestamp() :
                    #if periode.tempsDebut>=date_debut and periode.tempsFin<=date_fin :
                    #print(consommation_totale, ' + ', periode.consommation, ' = ', consommation_totale + periode.consommation)
                    consommation_totale = consommation_totale + periode.consommation
                else :

                    debut = periode.tempsDebut.timestamp()
                    fin = periode.tempsFin.timestamp()
                    if debut < date_debut.timestamp():
                        debut = date_debut.timestamp()
                    if fin > date_fin.timestamp():
                        fin = date_fin.timestamp()
                    C = self.puissance *(fin - debut) / 3600
                    """ if(periode.Equipement.id==11): 
                      print(consommation_totale, ' + ', C, ' = ', consommation_totale + C, " temps: ", (fin - debut) / 3600) """
                    consommation_totale = consommation_totale + C

        return consommation_totale



class PeriodeActivite(models.Model):
  tempsDebut = models.DateTimeField()
  tempsFin = models.DateTimeField(null=True, blank=True)
  Equipement = models.ForeignKey(Equipement,on_delete=models.CASCADE)
  consommation = models.FloatField(null=True, blank=True)
  class Meta:
    db_table = "quickstart_periode_activite"
  """ def __str__(self):
        return self.Equipement.nom """


  def calculer_consommation(self):
      debut = self.tempsDebut.replace(tzinfo=None).timestamp()
      fin = self.tempsFin.replace(tzinfo=None).timestamp()
      #debut = self.tempsDebut.timestamp()
      #fin = self.tempsFin.timestamp()

      heures_activite = (fin - debut) / 3600
      self.consommation = self.Equipement.puissance * heures_activite
      self.save()

class ExcelData(models.Model):
    column1 = models.FloatField()
    column2 = models.FloatField()
    
class Alerte(models.Model):
    type = models.CharField(max_length=32, null=True, blank=True)
    text = models.CharField(max_length=500, null=True, blank=True)
    localId = models.ForeignKey(Zone,on_delete=models.CASCADE, null=True, blank=True)
    equipementId= models.ForeignKey(Equipement,on_delete=models.CASCADE, null=True, blank=True)
    dateAlerte = models.DateTimeField(null=True, blank=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    valeur = models.FloatField(null=True, blank=True)
    notifie = models.BooleanField(default=False)
    vu = models.BooleanField(default=False)
    class Meta:
        db_table = "quickstart_alerte"

class Rapport(models.Model):
  alerte = models.ForeignKey(Alerte, on_delete=models.CASCADE, null=True, blank=True)
  redacteur = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  causes = models.CharField(max_length=2000, null=True, blank=True)
  solutions = models.CharField(max_length=2000, null=True, blank=True)
  risques = models.CharField(max_length=2000, null=True, blank=True)
  equipementsDemandes = models.CharField(max_length=2000, null=True, blank=True)
  equipementsNecessites = models.CharField(max_length=2000, null=True, blank=True)
  equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE, null=True, blank=True)
  dateRapport = models.DateTimeField(null=True, blank=True)
  vu = models.BooleanField(default=False)
  notifie = models.BooleanField(default=False)
  decision = models.CharField(max_length=2000, null=True, blank=True)
  class Meta:
    db_table = "quickstart_rapport"


class Sauvegarde(models.Model):
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE, null=True, blank=True)
    janvier = models.FloatField(null=True, blank=True)
    fevrier = models.FloatField(null=True, blank=True)
    mars = models.FloatField(null=True, blank=True)
    avril = models.FloatField(null=True, blank=True)
    mai = models.FloatField(null=True, blank=True)
    juin = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = "quickstart_sauvegarde"
class Historique(models.Model):
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE, null=True, blank=True)
    dateDebut = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateFin = models.DateTimeField(null=True, blank=True)
    decision = models.CharField(max_length=2000, null=True, blank=True)
    rapport = models.ForeignKey(Rapport, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "quickstart_historique"



