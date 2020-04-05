"""
from django.forms import ModelForm
from .models import RunningForm


class RunningForm(forms.Form):
    firstname = forms.CharField(label='Voornaam', max_length=100)
    lastname = forms.CharField(label='Achternaam', max_length=100)
    email = forms.EmailField(label='E-mailadres')
    formtype = forms.ChoiceField(label='Formulier type')



class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2',)
"""
