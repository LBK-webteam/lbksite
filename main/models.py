from django.db import models
from django.forms import ModelForm

from ckeditor.fields import RichTextField


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_text = RichTextField(blank=True, null=True)
    post_creation_date = models.DateTimeField()
    post_url = models.URLField(blank=True)

    def __str__(self):
        return self.post_title


class Page(models.Model):
    page_title = models.CharField(max_length=200, primary_key=True)
    page_text = RichTextField(blank=True, null=True)
    page_index = models.IntegerField(default=0)
    page_werkgroeplogo = models.ImageField('Icoon', upload_to='werkgroepen', default='werkgroepen/sport.png')

    def __str__(self):
        return self.page_title


class Vacancy(models.Model):
    company_name = models.CharField(max_length=200)
    company_logo = models.ImageField(blank=True)
    vacancy_function = models.CharField(max_length=200)
    vacancy_description = RichTextField()
    vacancy_url = models.URLField()

    class Meta:
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.vacancy_function + ' ' + self.company_name


class Event(models.Model):
    pub_date = models.DateTimeField('Event link online')
    event_title = models.CharField('Titel', max_length=200, primary_key=True)
    event_desc = models.TextField('Beschrijving')
    event_link = models.URLField('Link', max_length=200)
    event_price_nm = models.FloatField('Prijs niet-lid')
    event_price_m = models.FloatField('Prijs lid')
    event_location = models.CharField('Locatie', max_length=200)

    def __str__(self):
        return self.event_title


class EventReg(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    reg_firstname = models.CharField('Voornaam', max_length=200)
    reg_lastname = models.CharField('Achternaam', max_length=200)
    reg_email = models.EmailField('E-mail')
    reg_member = models.BooleanField('Lid van LBK')


class DBmember(models.Model):
    first_name = models.CharField('Voornaam', max_length=200)
    last_name = models.CharField('Achternaam', max_length=200)

    function = models.CharField('Functie', max_length=50, primary_key=True, choices=[
        ('Preses', 'Preses'),
        ('Vice-preses', 'Vice-preses'),
        ('Penningmeester', 'Penningmeester'),
        ('Secretaris', 'Secretaris'),
        ('Gnorgl verantwoordelijke', 'Gnorgl verantwoordelijke'),
        ('Gnorgl boekhouder', 'Gnorgl boekhouder'),
        ('Baarr verantwoordelijke', 'Baarr verantwoordelijke'),
        ('Baarr boekhouder', 'Baarr boekhouder'),
        ('Activiteiten verantwoordelijke', 'Activiteiten verantwoordelijke'),
        ('Sport verantwoordelijke', 'Sport verantwoordelijke'),
        ('Cultuur verantwoordelijke', 'Cultuur verantwoordelijke'),
        ('Internationaal verantwoordelijke', 'Internationaal verantwoordelijke'),
        ('Bedrijvenrelaties verantwoordelijke', 'Bedrijvenrelaties verantwoordelijke'),
        ('Onderwijs verantwoordelijke', 'Onderwijs verantwoordelijke'),
        ('Onderwijs secretaris', 'Onderwijs secretaris'),
        ('Logistiek verantwoordelijke', 'Logistiek verantwoordelijke'),
        ('Cursusdienst verantwoordelijke', 'Cursusdienst verantwoordelijke'),
        ('ICT verantwoordelijke', 'ICT-verantwoordelijke')
    ])

    email = models.EmailField('E-mail', null=True)
    phone_number = models.CharField('Gsm-nummer', max_length=20)
    profile_picture = models.ImageField('Profielfoto', upload_to='db')

    class Meta:
        verbose_name = 'DB member'

    def __str__(self):
        return self.function


class Running(models.Model):
    first_name = models.CharField('Voornaam', max_length=100)
    last_name = models.CharField('Achternaam', max_length=100)
    email = models.EmailField('E-mail')
    formtype = models.CharField('Type formulier', max_length=100, choices=[
        ('A', 'Formulier A'),
        ('B', 'Formulier B'),
        ('C', 'Formulier C')
    ])

    function = models.CharField('Functie', max_length=50, choices=[
        ('Preses', 'Preses'),
        ('Vice-preses', 'Vice-preses'),
        ('Penningmeester', 'Penningmeester'),
        ('Secretaris', 'Secretaris'),
        ('Gnorgl verantwoordelijke', 'Gnorgl verantwoordelijke'),
        ('Gnorgl boekhouder', 'Gnorgl boekhouder'),
        ('Baarr verantwoordelijke', 'Baarr verantwoordelijke'),
        ('Baarr boekhouder', 'Baarr boekhouder'),
        ('Activiteiten verantwoordelijke', 'Activiteiten verantwoordelijke'),
        ('Sport verantwoordelijke', 'Sport verantwoordelijke'),
        ('Cultuur verantwoordelijke', 'Cultuur verantwoordelijke'),
        ('Internationaal verantwoordelijke', 'Internationaal verantwoordelijke'),
        ('Bedrijvenrelaties verantwoordelijke', 'Bedrijvenrelaties verantwoordelijke'),
        ('Onderwijs verantwoordelijke', 'Onderwijs verantwoordelijke'),
        ('Onderwijs secretaris', 'Onderwijs secretaris'),
        ('Logistiek verantwoordelijke', 'Logistiek verantwoordelijke'),
        ('Cursusdienst verantwoordelijke', 'Cursusdienst verantwoordelijke'),
        ('ICT verantwoordelijke', 'ICT-verantwoordelijke')
    ], null=True, blank=True)
    workgroup = models.CharField('Werkgroep', max_length=50, choices=[
        ('Penning', 'Penning'),
        ('Communicatie', 'Communicatie'),
        ('Gnorgl', 'Gnorgl'),
        ('Baarr', 'Baarr'),
        ('Activiteiten', 'Activiteiten'),
        ('Sport', 'Sport'),
        ('Cultuur', 'Cultuur'),
        ('Internationaal', 'Internationaal'),
        ('Bedrijvenrelaties', 'Bedrijvenrelaties'),
        ('Onderwijs', 'Onderwijs'),
        ('Logistiek', 'Logistiek'),
        ('Cursusdienst', 'Cursusdienst'),
        ('ICT', 'ICT'),
        ('Onthaal', 'Onthaal'),
        ('Revue', 'Revue'),
        ('IFR', 'IFR'),
        ('Galabal', 'Galabal'),
        ('IAAS', 'IAAS'),
        ('Bloedserieus', 'Bloedserieus'),
    ], null=True, blank=True)
    motivation = models.TextField('Motivatie', null=True, blank=True)
    motivation_b = models.TextField('Motivatie (B)', null=True, blank=True)
    members = models.TextField('Leden van de werkgroep', null=True, blank=True)
    members_c = models.TextField('Leden van de lolploeg', null=True, blank=True)
    q1 = models.TextField('Bestaansreden LBK', null=True, blank=True)
    q2 = models.TextField('LBK in de toekomst', null=True, blank=True)
    q3 = models.TextField('Rol binnen LBK', null=True, blank=True)
    q4 = models.TextField('Verbetering/Focus', null=True, blank=True)
    q5 = models.TextField('Waarom jij?', null=True, blank=True)
    q1b = models.TextField('Verbetering LBK toekomst', null=True, blank=True)
    q2b = models.TextField('Samenwerking team', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.formtype

    class Meta:
        verbose_name = 'Form'


class RunningForm(ModelForm):
    class Meta:
        model = Running
        fields = '__all__'
