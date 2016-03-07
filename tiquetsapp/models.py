from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User


class Categoria(models.Model):

    nombre = models.CharField(
        max_length=31,
        editable=True,
    )

    def __str__(self):
        return self.nombre


class Tiquet(models.Model):

    ESTADOS = [
        ('CR', "Creado"),
        ('TR', "En trámite"),
        ('FI', "Finalizado"),
    ]

    time_stamp = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


    autor = models.ForeignKey(User, verbose_name="Autor")
    titulo = models.CharField(max_length=127)
    contenido = models.TextField(max_length=255)
    estado = models.CharField(max_length=2, choices=ESTADOS, default='CR')
    categoria = models.ForeignKey('Categoria', blank=True, null=True)

    def historico(self):
        return self.estado
    historico.admin_order_field = 'pub_date'
    historico.boolean = True
    historico.short_description = 'Revisa el historial de tu solicitud.'

    def tiquets_por_categoria(self):

        return self.categoria

    def __str__(self):
        return self.titulo


@python_2_unicode_compatible
class Comentario(models.Model):

    comentario = models.ForeignKey(Tiquet, related_name="comentarios")
    texto_comentario = models.TextField(max_length=255)

    def __str__(self):
        return self.texto_comentario
