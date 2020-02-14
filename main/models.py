from django.db import models

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

    def __str__(self):
        return self.page_title


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
        ('Bedrijvenrelaties vice-verantwoordelijke', 'Bedrijvenrelaties vice-verantwoordelijke'),
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
