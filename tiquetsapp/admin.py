from django.contrib import admin
from .models import Comentario, Tiquet, Categoria


class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 1


class TiquetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['titulo', 'autor']}),
        (None,               {'fields': ['contenido']}),
        ("Categorías:",      {'fields': ['categoria'], 'classes': ['collapse']}),
    ]
    inlines = [ComentarioInline]
    list_display = ('contenido', 'last_update', 'autor', 'categoria')
    list_filter = ['time_stamp', 'categoria']
    search_fields = ['contenido']

admin.site.register(Tiquet, TiquetAdmin)
admin.site.register(Categoria)