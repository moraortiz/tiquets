from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^categoria/$', views.listado_categorias, name='listado-categorias'), #categorías
    url(r'^categoria/detalle/(?P<id>\d+)/$', views.detalle_categoria,
        name='detalle-categoria'), #categoria única
    url(r'^tiquet/$', views.listado_tiquets, name='listado-tiquets'), #tiquets
    url(r'^tiquet/detalle/(\d+)/$', views.detalle_tiquet,
        name='detalle-tiquet'), #tiquet único
    #url(r'^usuario/(\d+)/$', views.usuario, name='usuario'), #tiquets
    url(r'^tiquet/nuevo/$', views.nuevo_tiquet, name='formulario'),
]