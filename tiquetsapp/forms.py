from django import forms
from .models import Tiquet, Comentario

class Formulario(forms.ModelForm):

    class Meta:
        model = Tiquet
        fields = ('titulo', 'contenido', 'autor')


class Comentario(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('autor', 'contenido')