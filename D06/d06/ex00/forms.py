# coding : utf8

from django import forms
from django.contrib.auth.models import User
from ex00.models import Tip


class InscriptionForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(
        required=True, widget=forms.PasswordInput, initial='')
    verif_password = forms.CharField(
        required=True, widget=forms.PasswordInput, initial='')

    def clean(self):
        # appliquer la validation de la classe mere
        form_data = super(InscriptionForm, self).clean()
        # recherche d'unicite
        u = User.objects.filter(username=form_data['username'])
        if len(u) > 0:
            self._errors['username'] = ["Le nom saisi est déjà pris"]
        if form_data['password'] != form_data['verif_password']:
            self._errors['password'] = [
                "Le mot de passe doit être identique dans les 2 champs password"]
        return form_data


class ConnectionForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(
        required=True, widget=forms.PasswordInput, initial='')


class TipForm(forms.ModelForm):
    """ formulaire pour la classe Tip """
    class Meta:
        model = Tip
    fields = ['contenu']
