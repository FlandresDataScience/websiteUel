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

# class GraduationProgram(models.Model):
#     # campos coletados de http://www.uel.br/prograd/?content=catalogo-cursos/catalogo_2020/cursos_graduacao.html
#     title = models.CharField(max_length=64)
#     description = models.CharField(max_length=280)
#     presentation = models.TextField()
#     respSecretary = models.ForeignKey(Secretary, on_delete=models.CASCADE, related_name="respSecretary")
#     # campos adicionais coletados de http://www.uel.br/portal/english/index.php/academics/undergraduate/ 

#     def __str__(self):
#         return f"{self.title}"

