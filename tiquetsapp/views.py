from django.shortcuts import get_object_or_404, render
from .models import Categoria, Tiquet
from django.contrib.auth.models import User
from .forms import Formulario
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
#             # Redirect to a success page.
#             return HttpResponse("You're logged in.")
#         else:
#             # Return a 'disabled account' error message
#             return HttpResponse("Your username and password didn't match.")
#     else:

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

def detalle_categoria(request, id):

    contenido = get_object_or_404(Categoria, pk=id)
    context = {'object': contenido}
    return render(request, 'tiquetsapp/detalle_categoria.html', context)

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
            return redirect('detalle-tiquet', tiquet.pk)
    else:
        form = Formulario()
    return render(request, 'tiquetsapp/editor.html', {'form': form})


# def acceso(request):
#     try:
#         m = Member.objects.get(username__exact=request.POST['username'])
#         if m.password == request.POST['password']:
#             request.session['member_id'] = m.id
#             return HttpResponse("You're logged in.")
#     except Member.DoesNotExist:
#         return HttpResponse("Your username and password didn't match.")
#
#
# def salida(request):
#     try:
#         del request.session['member_id']
#     except KeyError:
#         pass
#     return HttpResponse("You're logged out.")
