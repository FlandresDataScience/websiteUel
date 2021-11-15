from django.db import models

# Create your models here.

# Secretary was a table created with test purposes
class Secretary(models.Model):
    secretary = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.secretary}"
# Program was a table created with test purposes
class Program(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=280)
    presentation = models.TextField()
    respSecretary = models.ForeignKey(Secretary, on_delete=models.CASCADE, related_name="respSecretary")

    def __str__(self):
        return f"{self.title}"

class GraduationProgram(models.Model):
    # campos coletados de http://www.uel.br/prograd/?content=catalogo-cursos/catalogo_2020/cursos_graduacao.html
    title = models.CharField(max_length=64)
    creation = models.CharField(max_length=64)
    grade = models.CharField(max_length=64)
    profile = models.TextField()
    objective = models.TextField()
    atuation = models.TextField()
    system = models.CharField(max_length=64)
    durationMin = models.IntegerField(default=4)
    durationMax = models.IntegerField(default=8)
    shiftVacancies = models.CharField(max_length=64)
    # campos adicionais coletados de http://www.uel.br/portal/english/index.php/academics/undergraduate/ 
    language = models.CharField(max_length=64, default="Portuguesa")
    contact = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title} model-object"

class PostLato(models.Model):
    # campos coletados de https://www.sistemasweb.uel.br/index.php?contents=system/inscpos/index.php&pagina=view/ListarCursos.php 
    title = models.CharField(max_length=64)
    center = models.CharField(max_length=64)
    reference = models.CharField(max_length=64)
    # degree = models.CharField(max_length=64)
    profile = models.TextField()
    monthCost = models.IntegerField()
    duration = models.IntegerField(default=8)

    def __str__(self):
        return f"{self.title} model-object"

class PostStricto(models.Model):
    # campos (mestrado) coletados de https://www.sistemasweb.uel.br/index.php?contents=system/inscpos/index.php&pagina=view/ListarCursos.php&nv_curso=2&sq_nivel=1
    # campos (doutorado) https://www.sistemasweb.uel.br/index.php?contents=system/inscpos/index.php&pagina=view/ListarCursos.php
    title = models.CharField(max_length=64)
    center = models.CharField(max_length=64)
    reference = models.CharField(max_length=64)
    degree = models.CharField(max_length=64)
    creation = models.CharField(max_length=64) # resolucao
    profile = models.TextField()
    capes = models.IntegerField()
    concentration = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title} model-object"