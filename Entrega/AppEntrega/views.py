from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse

def inicio(request):   
    return render(request, "AppEntrega/index.html")

def alumnos(request):   
    return render(request, "AppEntrega/alumnos.html")

def profesores(request):   
    return render(request, "AppEntrega/profesores.html")

def curso(request):   
    return render(request, "AppEntrega/curso.html")


#def saludo(request):   
    return HttpResponse("Hola Coder")

#def mi_nombre(request, nombre):
    texto = f"Mi nombre es: {nombre}"
    return HttpResponse(texto)

#def contexto (request):
    dic = {"nombre": "Tomas", "ape": "Pujolle"}

    plantilla = loader.get_template('contexto.html')

    docu = plantilla.render(dic)
    return HttpResponse(docu)
