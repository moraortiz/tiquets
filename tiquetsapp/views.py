from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .models import Categoria, Tiquet
from django.contrib.auth.models import User
from .forms import Formulario, Comentario
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'tiquetsapp/index.html')

# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             return render(request, 'index')
#         else:
#             return render(request, 'login')
#     else:
#         return render(request, 'login')
#
# def logout(request):
#     try:
#         del request.session['member_id']
#     except KeyError:
#         pass
#     return render(request, 'index')

@login_required
def listado_categorias(request):
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


@login_required
def detalle_categoria(request, id):

    contenido = get_object_or_404(Categoria, pk=id)
    context = {'object': contenido}
    return render(request, 'tiquetsapp/detalle_categoria.html', context)


@login_required
def listado_tiquets(request):
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


@login_required
def detalle_tiquet(request, id):
    contenido = get_object_or_404(Tiquet, pk=id)
    context = {'object': contenido}
    return render(request, 'tiquetsapp/detalle_tiquet.html', context)


@login_required
def tiquets_autor(request, id):
    usuario = User.objects.get(id=id)
    listado = Tiquet.objects.all()
    context = {'object_list': listado}
    return render(request, 'tiquetsapp/autor.html', context)


@login_required
def nuevo_tiquet(request):
    form = Formulario()
    if request.method == "POST":
        form = Formulario(request.POST)
        if form.is_valid():
            tiquet = form.save()
            tiquet.save()
            return redirect('detalle-tiquet', tiquet.pk)
    else:
        form = Formulario()
    return render(request, 'tiquetsapp/editor.html', {'form': form})


@login_required
def comentario(request):
    form = Comentario()
    if request.method == "POST":
        form = Formulario(request.POST)
        if form.is_valid():
            comentario = form.save()
            comentario.save()
            return redirect('detalle-tiquet', comentario.pk)
    else:
        form = Formulario()
    return render('index', {'form': form})