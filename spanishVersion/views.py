from django.shortcuts import render
from django.http import HttpResponse

from .models import GraduationProgram, PostLato, PostStricto, Program, Secretary
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


def post(request): 
    clchList = PostLato.objects.filter(center="CLCH")
    # print(clchList)
    ccbList  = PostLato.objects.filter(center="CCB")
    print(ccbList)
    cceList  = PostLato.objects.filter(center="CCE")
    cesaList = PostLato.objects.filter(center="CESA")
    ccsList  = PostLato.objects.filter(center="CCS")
    cecaList = PostLato.objects.filter(center="CECA")
    ctuList  = PostLato.objects.filter(center="CTU")
    cefeList = PostLato.objects.filter(center="CEFE")
    return render(request, "spanishVersion/pos.html", {
        "clchList": clchList,
        "ccbList": ccbList,
        "cceList": cceList,
        "cesaList": cesaList,
        "ccsList": ccsList,
        "cecaList": cecaList,
        "ctuList": ctuList,
        "cefeList": cefeList,
    })

def pospage(request, pos_title):
    # print(grad_title)
    # requestedGrad = Program.objects.get(title=grad_title)
    requestedPos = PostLato.objects.get(title=pos_title)
    # print("..............................")
    # print(requestedGrad)
    return render(request, "spanishVersion/pos_program.html", {
      "requestedPos": requestedPos,  
    })

def mestrado(request): 
    mastersClch = PostStricto.objects.filter(degree="Mestre", center="CLCH")
    print(mastersClch)
    mastersCca  = PostStricto.objects.filter(degree="Mestre",center="CCA")
    mastersCcb  = PostStricto.objects.filter(degree="Mestre",center="CCB")
    print(mastersCcb)
    mastersCce  = PostStricto.objects.filter(degree="Mestre",center="CCE")
    mastersCesa = PostStricto.objects.filter(degree="Mestre",center="CESA")
    mastersCcs  = PostStricto.objects.filter(degree="Mestre",center="CCS")
    mastersCeca = PostStricto.objects.filter(degree="Mestre",center="CECA")
    mastersCtu  = PostStricto.objects.filter(degree="Mestre",center="CTU")
    mastersCefe = PostStricto.objects.filter(degree="Mestre",center="CEFE")
    return render(request, "spanishVersion/mestrado.html",  {
        "mastersClch": mastersClch, 
        "mastersCca": mastersCca,
        "mastersCcb": mastersCcb,   
        "mastersCce": mastersCce,   
        "mastersCesa": mastersCesa, 
        "mastersCcs": mastersCcs,   
        "mastersCeca": mastersCeca, 
        "mastersCtu": mastersCtu,   
        "mastersCefe": mastersCefe, 
})

def maspage(request, mas_title):
    requestedMas = PostStricto.objects.get(title=mas_title, degree="Mestre")
    return render(request, "spanishVersion/mas_program.html", {
      "requestedMas": requestedMas,  
    })

def doutorado(request): 
    doctorsClch = PostStricto.objects.filter(degree="Doutor",center="CLCH")
    doctorsCca  = PostStricto.objects.filter(degree="Doutor",center="CCA")
    doctorsCcb  = PostStricto.objects.filter(degree="Doutor",center="CCB")
    doctorsCce  = PostStricto.objects.filter(degree="Doutor",center="CCE")
    doctorsCeca = PostStricto.objects.filter(degree="Doutor",center="CECA")
    doctorsCesa = PostStricto.objects.filter(degree="Doutor",center="CESA")
    doctorsCcs  = PostStricto.objects.filter(degree="Doutor",center="CCS")
    doctorsCeca = PostStricto.objects.filter(degree="Doutor",center="CECA")
    doctorsCtu  = PostStricto.objects.filter(degree="Doutor",center="CTU")
    doctorsCefe = PostStricto.objects.filter(degree="Doutor",center="CEFE")
    return render(request, "spanishVersion/doutorado.html", {
        "doctorsClch": doctorsClch,
        "doctorsCca": doctorsCca,
        "doctorsCcb": doctorsCcb,
        "doctorsCce": doctorsCce,
        "doctorsCeca": doctorsCeca,
        "doctorsCesa": doctorsCesa,
        "doctorsCcs": doctorsCcs,
        "doctorsCeca": doctorsCeca,
        "doctorsCtu": doctorsCtu,
        "doctorsCefe": doctorsCefe,
    })

def docpage(request, doc_title):
    requestedDoc = PostStricto.objects.get(title=doc_title, degree="Doutor")
    return render(request, "spanishVersion/doc_program.html", {
      "requestedDoc": requestedDoc,  
    })

def pesquisa(request): return render(request, "spanishVersion/pesquisa.html")
def laboratorios(request): return render(request, "spanishVersion/laboratorios.html")
def extensao(request): return render(request, "spanishVersion/extensao.html")
def assessoria(request): return render(request, "spanishVersion/acessoria.html")
def guia_estudante(request): return render(request, "spanishVersion/guia_estudante.html")
def biblioteca(request): return render(request, "spanishVersion/biblioteca.html")
