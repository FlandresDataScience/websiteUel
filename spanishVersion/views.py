from django.shortcuts import render
from django.http import HttpResponse

from .models import GraduationProgram, Program, Secretary
# Create your views here.

# renderiza o index.html no path ""
def index(request):
    loadProgram = Program.objects.all()
    # print(loadProgram[1].title)

    return render(request, "spanishVersion/index.html", {
        "loadProgram": loadProgram,
    })
def program(request, program_title):
    # print(program_title)
    requestedProgram = Program.objects.get(title=program_title)
    # print(requestedProgram.respSecretary.id)
    reqProSecretary = Secretary.objects.get(pk=requestedProgram.respSecretary.id)
    print(reqProSecretary.email)
    return render(request, "spanishVersion/program.html", {
        "requestedProgram": requestedProgram,
        "reqProSecretary": reqProSecretary,
    })


def historia(request): return render(request, "spanishVersion/Historia.html")
def corpos(request): return render(request, "spanishVersion/Corpos_de_apoio.html")
def orgaos(request): return render(request, "spanishVersion/Orgaos_apoio_saude.html")
def canais(request): return render(request, "spanishVersion/canais_comunicacao.html")
def arte(request): return render(request, "spanishVersion/Arte_cultura.html")
def esportes(request): return render(request, "spanishVersion/esportes_e_condicionamento.html")
def vida(request): return render(request, "spanishVersion/vida_de_estudante.html")


def graduacao(request): 
    gradList = GraduationProgram.objects.all()
    return render(request, "spanishVersion/graduacao.htm", {
        "gradList": gradList,
    })


def gradpage(request, grad_title):
    # print(grad_title)
    # requestedGrad = Program.objects.get(title=grad_title)
    requestedGrad = GraduationProgram.objects.get(title=grad_title)
    # print("..............................")
    # print(requestedGrad)
    return render(request, "spanishVersion/grad_program.html", {
      "requestedGrad": requestedGrad,  
    })


def post(request): return render(request, "spanishVersion/pos.html")
def mestrado(request): return render(request, "spanishVersion/mestrado.html")
def doutorado(request): return render(request, "spanishVersion/doutorado.html")
def pesquisa(request): return render(request, "spanishVersion/pesquisa.html")
def laboratorios(request): return render(request, "spanishVersion/laboratorios.html")
def extensao(request): return render(request, "spanishVersion/extensao.html")
def assessoria(request): return render(request, "spanishVersion/acessoria.html")
def guia_estudante(request): return render(request, "spanishVersion/guia_estudante.html")
def biblioteca(request): return render(request, "spanishVersion/biblioteca.html")
