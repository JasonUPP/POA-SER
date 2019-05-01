from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='AnteProyecto'),
    #AP
    path('nuevoAP/', views.crearap, name='crearap'),
    path('totalA/<int:id_anteproyecto>', views.tf, name='tf'),
    path('verAP/', views.verap, name='verap'),
    path('delAP/<int:id_anteproyecto>/', views.delap, name='delap'),
    path('editAP/<int:id_anteproyecto>/', views.editap, name='editap'),
    #ApImg
    path('InsertarAP/', views.antePI, name='insertap'),
    #Fila
    path('nuevaF/', views.crearf, name="crearf"),
    path('verF/<int:id_anteproyecto>', views.verf, name="verf"),
    path('delF/<int:id_fila>/', views.delf, name="delf"),
    path('editF/<int:id_fila>/', views.editf, name="editf"),
    #capitulos
    path('Opciones/', views.iniciopc, name="iniciopc"),
    path('Capitulos/', views.vercap, name="vercap"),
    path('NuevoCapitulo/', views.crearcap, name="crearcap"),
    path('delcap/<int:id_capitulo>/', views.delcap, name="delcap"),
    path('editcap/<int:id_capitulo>/', views.editcap, name='editcap'),
    #Conceptos
    path('Conceptos/', views.vercon, name="vercon"),
    path('ajax/load-conc/', views.loadConc, name="loadc"),
    path('NuevoConcepto/', views.crearcon, name="crearcon"),
    path('delConcepto/<int:id_concepto>/', views.delcon, name="delcon"),
    path('editConcepto/<int:id_concepto>/', views.editcon, name='editcon'),
    #partidagenerica
    path('PartidasGenericas/', views.verpg, name="verpg"),
    path('ajax/load-pg/', views.loadpg, name="loadpg"),
    path('NuevaPartidaGenerica/', views.crearpg, name="crearpg"),
    path('delPG/<int:id_partidagenerica>/', views.delpg, name="delpg"),
    path('editPG/<int:id_partidagenerica>/', views.editpg, name="editpg"),
    #partidaespecifica
    path('PartidasEspecificas/', views.verpe, name="verpe"),
    path('ajax/load-pe/', views.loadpe, name="loadpe"),
    path('NuevaPartidaEspecifica/', views.crearpe, name="crearpe"),
    path('delPE/<int:id_partidaespecifica>/', views.delpe, name="delpe"),
    path('editPE/<int:id_partidaespecifica>/', views.editpe, name="editpe"),
]
