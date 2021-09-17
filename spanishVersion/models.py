from django.db import models

# Create your models here.
class Secretary(models.Model):
    secretary = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.secretary}"

class Program(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=280)
    presentation = models.TextField()
    respSecretary = models.ForeignKey(Secretary, on_delete=models.CASCADE, related_name="respSecretary")

    def __str__(self):
        return f"{self.title}"
