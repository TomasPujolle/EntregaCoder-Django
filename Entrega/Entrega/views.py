from django.http import HttpResponse
from django.template import loader

 

def saludo(request):   
    return HttpResponse("Hola Coder")

def mi_nombre(request, nombre):
    texto = f"Mi nombre es: {nombre}"
    return HttpResponse(texto)

def contexto (request):
    dic = {"nombre": "Tomas", "ape": "Pujolle"}

    plantilla = loader.get_template('index.html')

    docu = plantilla.render(dic)
    return HttpResponse(docu)

