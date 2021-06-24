from django.urls import path
from .views import  form_mod_vehiculo, form_vehiculo, home,listaseries

urlpatterns = [
    path('',home,name="home"),
    path('listaseries/',listaseries,name="listaseries"),
    path('form-vehiculo',form_vehiculo,name="form_vehiculo"),
    path('form-mod-vehiculo/<id>',form_mod_vehiculo,name="form_mod_vehiculo")
]