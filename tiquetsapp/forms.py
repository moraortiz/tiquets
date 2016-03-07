from django import forms

from .models import Tiquet

class Formulario(forms.ModelForm):

    class Meta:
        model = Tiquet
        fields = ('titulo', 'contenido',)