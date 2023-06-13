from django.shortcuts import render
from .models import Curso, Profesor, Alumno
from .forms import BuscaCursoForm

def inicio(request):   
    return render(request, "AppEntrega/index.html")

def alumnos(request):   
     if request.method == 'POST':
        alumno =  Alumno(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'])
        alumno.save()
        return render(request, "AppEntrega/alumnos_bien.html")
     return render(request,"AppEntrega/alumnos.html")

def profesores(request):   
    if request.method == 'POST':
        profesor =  Profesor(nombre=request.POST['nombre'], apellido=request.POST['apellido'], materia=request.POST['materia'], email=request.POST['email'])
        profesor.save()
        return render(request, "AppEntrega/profesores_bien.html")
    return render(request,"AppEntrega/profesores.html")


def curso(request):
      
      if request.method == 'POST':
        curso =  Curso(nombre=request.POST['nombre'], camada=request.POST['camada'])
        curso.save()
        return render(request, "AppEntrega/curso_bien.html")
      return render(request,"AppEntrega/curso.html")

def buscar_curso(request):
    if request.method == "POST":
        busca_curso = BuscaCursoForm(request.POST)

        if busca_curso.is_valid():
            info = busca_curso.cleaned_data
            cursos = Curso.objects.filter(nombre=info["curso"])
            return render(request, "AppEntrega/lista_curso.html", {"cursos": cursos})
    else:
        busca_curso = BuscaCursoForm()
        return render(request, "AppEntrega/buscar_curso.html", {"miFormulario": busca_curso})