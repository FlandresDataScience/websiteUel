from django.shortcuts import render
from django.http import HttpResponse

from .models import Program, Secretary
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