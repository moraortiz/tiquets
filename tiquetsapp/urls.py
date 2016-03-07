from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^categoria/$', views.categorias, name='listado-categorias'), #categorías
    url(r'^categoria/(?P<id>\d+)/$', views.detalle_categoria,
        name='detalle-categoria'), #categoria única
    url(r'^tiquet/$', views.tiquets, name='listado-tiquets'), #tiquets
    url(r'^tiquet/(\d+)/$', views.detalle_tiquet,
        name='detalle-tiquet'), #tiquet único
    url(r'^usuario/(\d+)/$', views.tiquets, name='listado-tiquets'), #tiquets
    url(r'^tiquet/nuevo/$', views.nuevo_tiquet, name='formulario'),
]