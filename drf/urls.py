"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from nsqk import views
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth import views as auth_views

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Documentación API, NSQK',
        default_version='v1',
        description='NSQK, aplicación en DJANGO',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='user@test.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.pagina_inicio, name='pagina_inicio'),
    path('nsqk/', include('nsqk.urls')), # URL's para aplicación principal
    
    #URL's vistas de lista
    # path('listado_autores', views.listado_autores, name='listado_autores'),
    # path('listado_comunas', views.listado_comunas, name='listado_lectores'),
    # path('listado_lectores', views.listado_lectores, name='listado_lectres'),
    # path('listado_libros', views.listado_libros, name='lsitado_libros'),
    
    # URL's para documentación de API
    path('apidocs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # URL's de autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
]
