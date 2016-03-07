from django.shortcuts import get_object_or_404, render
from .models import Categoria, Tiquet
from django.contrib.auth.models import User
from .forms import Formulario
from django.shortcuts import redirect


def index(request):
    return render(request, 'tiquetsapp/index.html')

def categorias(request):
    listado = Categoria.objects.all()
    try:
        listado[0]
    except IndexError:
        return render(request, 'tiquetsapp/categorias.html', {
            'listado': listado,
            'error_message': "Aún no hay categorías creadas.",
        })
    context = {'object_list': listado}
    return render(request, 'tiquetsapp/categorias.html', context)

def detalle_categoria(request, id):

    contenido = get_object_or_404(Categoria, pk=id)
    context = {'object': contenido}
    return render(request, 'tiquetsapp/detalle_categoria.html', context)

def tiquets(request):
    listado = Tiquet.objects.all()
    try:
        listado[0]
    except IndexError:
        return render(request, 'tiquetsapp/tiquets.html', {
            'listado': listado,
            'error_message': "No hay tíquets en esta categoría.",
        })
    context = {'object_list': listado}
    return render(request, 'tiquetsapp/tiquets.html', context)

def detalle_tiquet(request, id):
    contenido = get_object_or_404(Tiquet, pk=id)
    context = {'object': contenido}
    return render(request, 'tiquetsapp/detalle_tiquet.html', context)


def tiquets_autor(request, id):
    usuario = User.objects.get(id=id)
    listado = Tiquet.objects.all()
    context = {'object_list': listado}
    return render(request, 'tiquetsapp/autor.html', context)


def nuevo_tiquet(request):
    form = Formulario()
    if request.method == "POST":
        form = Formulario(request.POST)
        if form.is_valid():
            tiquet = form.save()
            tiquet.save()
            return redirect('detalle_tiquet', pk=tiquet.pk)
    else:
        form = Formulario()
    return render(request, 'tiquetsapp/editor.html', {'form': form})
