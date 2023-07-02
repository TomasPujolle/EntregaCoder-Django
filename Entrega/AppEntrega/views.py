from django.shortcuts import render, redirect
from .models import Curso, Profesor, Alumno
from .forms import BuscaCursoForm, BuscaAlumnoForm, BuscaProfesorForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from AppEntrega import forms
from django.contrib.auth.views import LogoutView
from django.views.generic.detail import DetailView


def inicio(request): 
    return render(request, "AppEntrega/index.html")


def alumnos(request):   
     if request.method == 'POST':
        alumno =  Alumno(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'])
        alumno.save()
        return render(request, "AppEntrega/alumnos_bien.html")
     return render(request,"AppEntrega/alumnos.html")

def mostrar_alumnos(request):
    alumnos = Alumno.objects.all()
    contexto= {"alumnos":alumnos} 
    return render(request, "AppEntrega/mostrar_alumnos.html",contexto)

def buscar_alumno(request):
    if request.method == "POST":
        busca_alumno = BuscaAlumnoForm(request.POST)

        if busca_alumno.is_valid():
            info = busca_alumno.cleaned_data
            alumnos = Alumno.objects.filter(nombre=info["alumno"])
            return render(request, "AppEntrega/lista_alumno.html", {"alumnos": alumnos})
    else:
        busca_alumno = BuscaAlumnoForm()
        return render(request, "AppEntrega/buscar_alumno.html", {"miFormulario": busca_alumno})

def eliminar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    alumno = Alumno.objects.all()
    contexto = {"alumnos": alumno}
    return render (request, "AppEntrega/mostrar_alumnos.html", contexto)




def profesores(request):   
    if request.method == 'POST':
        profesor =  Profesor(nombre=request.POST['nombre'], apellido=request.POST['apellido'], materia=request.POST['materia'], email=request.POST['email'])
        profesor.save()
        return render(request, "AppEntrega/profesores_bien.html")
    return render(request,"AppEntrega/profesores.html")

def mostrar_profesores(request):
    profesores = Profesor.objects.all()
    contexto= {"profesores":profesores} 
    return render(request, "AppEntrega/mostrar_profesores.html",contexto)

def buscar_profesor(request):
    if request.method == "POST":
        busca_profesor = BuscaProfesorForm(request.POST)

        if busca_profesor.is_valid():
            info = busca_profesor.cleaned_data
            profesor = Profesor.objects.filter(nombre=info["profesor"])
            return render(request, "AppEntrega/lista_profesor.html", {"profesor": profesor})
    else:
        busca_profesor = BuscaProfesorForm()
        return render(request, "AppEntrega/buscar_profesor.html", {"miFormulario": busca_profesor})

def eliminar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    profesor = Profesor.objects.all()
    contexto = {"profesores": profesor}
    return render (request, "AppEntrega/mostrar_profesores.html", contexto)



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

def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto= {"cursos":cursos} 
    return render(request, "AppEntrega/mostrar_cursos.html",contexto)

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    curso = Curso.objects.all()
    contexto = {"cursos": curso}
    return render (request, "AppEntrega/mostrar_cursos.html", contexto)



def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return render(request, "AppEntrega/login.html", {"mensaje": "Datos incorrectos"})

    form = AuthenticationForm()
    return render(request, "AppEntrega/login.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = forms.RegistroUsuarioForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'AppEntrega/registro.html', {'form':form})
    form = forms.RegistroUsuarioForm()
    return render(request, 'AppEntrega/registro.html', {'form':form})

class Logout(LogoutView):
    template_name = 'AppEntrega/logout.html'

class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppEntrega/curso_detalle.html"

class AlumnoDetalle(DetailView):
    model = Alumno
    template_name = "AppEntrega/alumno_detalle.html"

class ProfesorDetalle(DetailView):
    model = Profesor
    template_name = "AppEntrega/profesor_detalle.html"