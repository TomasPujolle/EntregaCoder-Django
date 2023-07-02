from django.urls import path
from AppEntrega import views
from .views import inicio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', inicio, name='inicio'),

    path('alumnos/', views.alumnos, name='alumnos'),
    path('mostrar_alumnos/', views.mostrar_alumnos, name='mostrar_alumnos'),
    path('buscar-alumno/', views.buscar_alumno, name="buscar_alumno"),
    path('eliminar-alumno/<id>/', views.eliminar_alumno, name="eliminar_alumno"),
    path('alumno_detalle/<pk>/', views.AlumnoDetalle.as_view(), name="alumno_detalle"),

    path('profesores/', views.profesores, name='profesores'),
    path('mostrar_profesores/', views.mostrar_profesores, name='mostrar_profesores'),
    path('buscar-profesor/', views.buscar_profesor, name="buscar_profesor"),
    path('eliminar-profesor/<id>/', views.eliminar_profesor, name="eliminar_profesor"),
    path('profesor_detalle/<pk>/', views.ProfesorDetalle.as_view(), name="profesor_detalle"),

    path('curso/', views.curso, name='curso'),
    path('mostrar_cursos/', views.mostrar_cursos, name='mostrar_cursos'),
    path('buscar_curso/', views.buscar_curso, name="buscar_curso"),
    path('eliminar-curso/<id>/', views.eliminar_curso, name="eliminar_curso"),
    path('curso_detalle/<pk>/', views.CursoDetalle.as_view(), name="curso_detalle"),


    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.Logout.as_view(), name='logout'),
]
 
