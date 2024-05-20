# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCeleryBeatClockedschedule(models.Model):
    clocked_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_clockedschedule'


class DjangoCeleryBeatCrontabschedule(models.Model):
    minute = models.CharField(max_length=240)
    hour = models.CharField(max_length=96)
    day_of_week = models.CharField(max_length=64)
    day_of_month = models.CharField(max_length=124)
    month_of_year = models.CharField(max_length=64)
    timezone = models.CharField(max_length=63)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_crontabschedule'


class DjangoCeleryBeatIntervalschedule(models.Model):
    every = models.IntegerField()
    period = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_intervalschedule'


class DjangoCeleryBeatPeriodictask(models.Model):
    name = models.CharField(unique=True, max_length=200)
    task = models.CharField(max_length=200)
    args = models.TextField()
    kwargs = models.TextField()
    queue = models.CharField(max_length=200, blank=True, null=True)
    exchange = models.CharField(max_length=200, blank=True, null=True)
    routing_key = models.CharField(max_length=200, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    last_run_at = models.DateTimeField(blank=True, null=True)
    total_run_count = models.PositiveIntegerField()
    date_changed = models.DateTimeField()
    description = models.TextField()
    crontab = models.ForeignKey(DjangoCeleryBeatCrontabschedule, models.DO_NOTHING, blank=True, null=True)
    interval = models.ForeignKey(DjangoCeleryBeatIntervalschedule, models.DO_NOTHING, blank=True, null=True)
    solar = models.ForeignKey('DjangoCeleryBeatSolarschedule', models.DO_NOTHING, blank=True, null=True)
    one_off = models.BooleanField()
    start_time = models.DateTimeField(blank=True, null=True)
    priority = models.PositiveIntegerField(blank=True, null=True)
    headers = models.TextField()
    clocked = models.ForeignKey(DjangoCeleryBeatClockedschedule, models.DO_NOTHING, blank=True, null=True)
    expire_seconds = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictask'


class DjangoCeleryBeatPeriodictasks(models.Model):
    ident = models.AutoField(primary_key=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictasks'


class DjangoCeleryBeatSolarschedule(models.Model):
    event = models.CharField(max_length=24)
    latitude = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    longitude = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        managed = False
        db_table = 'django_celery_beat_solarschedule'
        unique_together = (('event', 'latitude', 'longitude'),)


class DjangoCeleryResultsChordcounter(models.Model):
    sub_tasks = models.TextField()
    count = models.PositiveIntegerField()
    group_id = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'django_celery_results_chordcounter'


class DjangoCeleryResultsGroupresult(models.Model):
    group_id = models.CharField(unique=True, max_length=255)
    date_created = models.DateTimeField()
    date_done = models.DateTimeField()
    content_type = models.CharField(max_length=128)
    content_encoding = models.CharField(max_length=64)
    result = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_results_groupresult'


class DjangoCeleryResultsTaskresult(models.Model):
    task_id = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=50)
    content_type = models.CharField(max_length=128)
    content_encoding = models.CharField(max_length=64)
    result = models.TextField(blank=True, null=True)
    date_done = models.DateTimeField()
    traceback = models.TextField(blank=True, null=True)
    meta = models.TextField(blank=True, null=True)
    task_args = models.TextField(blank=True, null=True)
    task_kwargs = models.TextField(blank=True, null=True)
    task_name = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    worker = models.CharField(max_length=100, blank=True, null=True)
    periodic_task_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_results_taskresult'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class QuickstartAlerte(models.Model):
    text = models.CharField(max_length=500, blank=True, null=True)
    equipementid = models.ForeignKey('QuickstartEquipement', models.DO_NOTHING, db_column='equipementId_id', blank=True, null=True)  # Field name made lowercase.
    localid = models.ForeignKey('QuickstartZone', models.DO_NOTHING, db_column='localId_id', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=32, blank=True, null=True)
    datealerte = models.DateTimeField(db_column='dateAlerte', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='userID_id', blank=True, null=True)  # Field name made lowercase.
    notifie = models.BooleanField()
    valeur = models.FloatField(blank=True, null=True)
    vu = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'quickstart_alerte'


class QuickstartBatiment(models.Model):
    nombatiment = models.CharField(db_column='nomBatiment', max_length=500)  # Field name made lowercase.
    typebatiment = models.CharField(db_column='typeBatiment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quickstart_batiment'


class QuickstartEquipement(models.Model):
    nom = models.CharField(max_length=500)
    etat = models.CharField(max_length=100)
    categorie = models.CharField(max_length=500, blank=True, null=True)
    puissance = models.FloatField(blank=True, null=True)
    zonee = models.ForeignKey('QuickstartZone', models.DO_NOTHING, db_column='zoneE_id')  # Field name made lowercase.
    type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'quickstart_equipement'


class QuickstartEtage(models.Model):
    surface = models.FloatField(blank=True, null=True)
    batimentid = models.ForeignKey(QuickstartBatiment, models.DO_NOTHING, db_column='batimentId_id')  # Field name made lowercase.
    nometage = models.CharField(db_column='nomEtage', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quickstart_etage'


class QuickstartExceldata(models.Model):
    column1 = models.FloatField()
    column2 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'quickstart_exceldata'


class QuickstartHistorique(models.Model):
    datefin = models.DateTimeField(db_column='dateFin', blank=True, null=True)  # Field name made lowercase.
    decision = models.CharField(max_length=2000, blank=True, null=True)
    equipement = models.ForeignKey(QuickstartEquipement, models.DO_NOTHING, blank=True, null=True)
    rapport = models.ForeignKey('QuickstartRapport', models.DO_NOTHING, blank=True, null=True)
    datedebut = models.DateTimeField(db_column='dateDebut', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quickstart_historique'


class QuickstartPeriodeactivite(models.Model):
    tempsfin = models.DateTimeField(db_column='tempsFin', blank=True, null=True)  # Field name made lowercase.
    consommation = models.FloatField(blank=True, null=True)
    equipement = models.ForeignKey(QuickstartEquipement, models.DO_NOTHING, db_column='Equipement_id')  # Field name made lowercase.
    tempsdebut = models.DateTimeField(db_column='tempsDebut', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quickstart_periodeactivite'


class QuickstartPeriodeactivit(models.Model):
    tempsdebut = models.DateTimeField(db_column='tempsDebut')  # Field name made lowercase.
    tempsfin = models.DateTimeField(db_column='tempsFin', blank=True, null=True)  # Field name made lowercase.
    consommation = models.FloatField(blank=True, null=True)
    equipement = models.ForeignKey(QuickstartEquipement, models.DO_NOTHING, db_column='Equipement_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quickstart_periodeactivité'


class QuickstartProfileuser(models.Model):
    role = models.CharField(max_length=30)
    userid = models.OneToOneField(AuthUser, models.DO_NOTHING, db_column='userId_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quickstart_profileuser'


class QuickstartRapport(models.Model):
    causes = models.CharField(max_length=2000, blank=True, null=True)
    solutions = models.CharField(max_length=2000, blank=True, null=True)
    risques = models.CharField(max_length=2000, blank=True, null=True)
    equipementsdemandes = models.CharField(db_column='equipementsDemandes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    equipementsnecessites = models.CharField(db_column='equipementsNecessites', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    alerte = models.ForeignKey(QuickstartAlerte, models.DO_NOTHING, blank=True, null=True)
    redacteur = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    equipement = models.ForeignKey(QuickstartEquipement, models.DO_NOTHING, blank=True, null=True)
    daterapport = models.DateTimeField(db_column='dateRapport', blank=True, null=True)  # Field name made lowercase.
    notifie = models.BooleanField()
    vu = models.BooleanField()
    decision = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quickstart_rapport'


class QuickstartSauvegarde(models.Model):
    janvier = models.FloatField(blank=True, null=True)
    fevrier = models.FloatField(blank=True, null=True)
    mars = models.FloatField(blank=True, null=True)
    avril = models.FloatField(blank=True, null=True)
    mai = models.FloatField(blank=True, null=True)
    juin = models.FloatField(blank=True, null=True)
    equipement = models.ForeignKey(QuickstartEquipement, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quickstart_sauvegarde'


class QuickstartZone(models.Model):
    nomlocal = models.CharField(db_column='nomLocal', max_length=500)  # Field name made lowercase.
    etagez = models.ForeignKey(QuickstartEtage, models.DO_NOTHING, db_column='etageZ_id')  # Field name made lowercase.
    surface = models.FloatField(blank=True, null=True)
    maxh = models.FloatField(db_column='maxH', blank=True, null=True)  # Field name made lowercase.
    maxt = models.FloatField(db_column='maxT', blank=True, null=True)  # Field name made lowercase.
    minh = models.FloatField(db_column='minH', blank=True, null=True)  # Field name made lowercase.
    mint = models.FloatField(db_column='minT', blank=True, null=True)  # Field name made lowercase.
    typelocal = models.CharField(db_column='typeLocal', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quickstart_zone'


class TachesAlerte(models.Model):
    type = models.CharField(max_length=32, blank=True, null=True)
    text = models.CharField(max_length=500, blank=True, null=True)
    datealerte = models.DateTimeField(db_column='dateAlerte', blank=True, null=True)  # Field name made lowercase.
    valeur = models.FloatField(blank=True, null=True)
    notifie = models.BooleanField()
    vu = models.BooleanField()
    userid = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='userID_id', blank=True, null=True)  # Field name made lowercase.
    equipementid = models.ForeignKey('TachesEquipement', models.DO_NOTHING, db_column='equipementId_id', blank=True, null=True)  # Field name made lowercase.
    localid = models.ForeignKey('TachesZone', models.DO_NOTHING, db_column='localId_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taches_alerte'


class TachesBatiment(models.Model):
    nombatiment = models.CharField(db_column='nomBatiment', max_length=500)  # Field name made lowercase.
    typebatiment = models.CharField(db_column='typeBatiment', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taches_batiment'


class TachesEquipement(models.Model):
    nom = models.CharField(max_length=500)
    etat = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    categorie = models.CharField(max_length=500, blank=True, null=True)
    puissance = models.FloatField(blank=True, null=True)
    zonee = models.ForeignKey('TachesZone', models.DO_NOTHING, db_column='zoneE_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taches_equipement'


class TachesEtage(models.Model):
    surface = models.FloatField(blank=True, null=True)
    nometage = models.CharField(db_column='nomEtage', max_length=500, blank=True, null=True)  # Field name made lowercase.
    batimentid = models.ForeignKey(TachesBatiment, models.DO_NOTHING, db_column='batimentId_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taches_etage'


class TachesExceldata(models.Model):
    column1 = models.FloatField()
    column2 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'taches_exceldata'


class TachesHistorique(models.Model):
    datedebut = models.DateTimeField(db_column='dateDebut', blank=True, null=True)  # Field name made lowercase.
    datefin = models.DateTimeField(db_column='dateFin', blank=True, null=True)  # Field name made lowercase.
    decision = models.CharField(max_length=2000, blank=True, null=True)
    equipement = models.ForeignKey(TachesEquipement, models.DO_NOTHING, blank=True, null=True)
    rapport = models.ForeignKey('TachesRapport', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taches_historique'


class TachesPeriodeactivite(models.Model):
    tempsdebut = models.DateTimeField(db_column='tempsDebut')  # Field name made lowercase.
    tempsfin = models.DateTimeField(db_column='tempsFin', blank=True, null=True)  # Field name made lowercase.
    consommation = models.FloatField(blank=True, null=True)
    equipement = models.ForeignKey(TachesEquipement, models.DO_NOTHING, db_column='Equipement_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taches_periodeactivite'


class TachesProfileuser(models.Model):
    role = models.CharField(max_length=30)
    userid = models.OneToOneField(AuthUser, models.DO_NOTHING, db_column='userId_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taches_profileuser'


class TachesRapport(models.Model):
    causes = models.CharField(max_length=2000, blank=True, null=True)
    solutions = models.CharField(max_length=2000, blank=True, null=True)
    risques = models.CharField(max_length=2000, blank=True, null=True)
    equipementsdemandes = models.CharField(db_column='equipementsDemandes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    equipementsnecessites = models.CharField(db_column='equipementsNecessites', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    daterapport = models.DateTimeField(db_column='dateRapport', blank=True, null=True)  # Field name made lowercase.
    vu = models.BooleanField()
    notifie = models.BooleanField()
    alerte = models.ForeignKey(TachesAlerte, models.DO_NOTHING, blank=True, null=True)
    equipement = models.ForeignKey(TachesEquipement, models.DO_NOTHING, blank=True, null=True)
    redacteur = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taches_rapport'


class TachesSauvegarde(models.Model):
    janvier = models.FloatField(blank=True, null=True)
    fevrier = models.FloatField(blank=True, null=True)
    mars = models.FloatField(blank=True, null=True)
    avril = models.FloatField(blank=True, null=True)
    mai = models.FloatField(blank=True, null=True)
    juin = models.FloatField(blank=True, null=True)
    equipement = models.ForeignKey(TachesEquipement, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taches_sauvegarde'


class TachesZone(models.Model):
    nomlocal = models.CharField(db_column='nomLocal', max_length=500)  # Field name made lowercase.
    typelocal = models.CharField(db_column='typeLocal', max_length=500, blank=True, null=True)  # Field name made lowercase.
    surface = models.FloatField(blank=True, null=True)
    mint = models.FloatField(db_column='minT', blank=True, null=True)  # Field name made lowercase.
    maxt = models.FloatField(db_column='maxT', blank=True, null=True)  # Field name made lowercase.
    minh = models.FloatField(db_column='minH', blank=True, null=True)  # Field name made lowercase.
    maxh = models.FloatField(db_column='maxH', blank=True, null=True)  # Field name made lowercase.
    etagez = models.ForeignKey(TachesEtage, models.DO_NOTHING, db_column='etageZ_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taches_zone'
