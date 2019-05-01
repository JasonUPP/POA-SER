from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', views.index, name='index'),


    #path('registrar/', views.usuario_view, name='registrar'),
    #path('listar/', views.usuario_list, name='listar'),
    #path('editar/<int:id_usuario>/' , views.usuario_edit, name='editar'),
    #path('eliminar/<int:id_usuario>/' , views.usuario_delete, name='eliminar'),


    path('signup/', views.SignUp.as_view(), name='signup'),
    path('list/', login_required(views.user_list), name='list'),
    path('edit/<int:id_user>/' , login_required(views.user_edit), name='edit'),
    path('delete/<int:id_user>/' , login_required(views.user_delete), name='delete'),
]
