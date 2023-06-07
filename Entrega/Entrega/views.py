from django.http import HttpResponse
from django.template import Template, Context

 

def saludo(request):   
    return HttpResponse("Hola Coder")

def mi_nombre(request, nombre):
    texto = f"Mi nombre es: {nombre}"
    return HttpResponse(texto)

def contexto (request):
    dic = {"nombre": "Tomas", "ape": "Pujolle"}

    mi_html = open('./Entrega/plantillas/index.html')

    plantilla = Template(mi_html.read())

    mi_html.close()

    contexto = Context(dic)

    docu = plantilla.render(contexto)

    return HttpResponse(docu)
