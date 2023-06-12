from django.urls import path
from .views import inicio, alumnos, profesores, curso

urlpatterns = [

    path('', inicio, name='inicio'),
    path('alumnos/', alumnos, name='alumnos'),
    path('profesores/', profesores, name='profesores'),
    path('curso/', curso, name='curso'),
   
]
 