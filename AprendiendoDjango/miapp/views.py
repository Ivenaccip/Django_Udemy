from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    html = """
    <h1>Inicio</h1>
    <p>Años hasta el 2050:</p>
    <ul>
    """
    year = 2023
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    return HttpResponse(html)

def hola_Mundo(request):
    return HttpResponse("""
    <h1>Hola mundo con Django!!</h1>
    <h3>Soy Leonardo Montaño </h3>
    """)

def pagina(request):
    return HttpResponse("""
    <h1>Página de mi web</h1>
    <p> Creado por Leonardo Medina</p>
    """)