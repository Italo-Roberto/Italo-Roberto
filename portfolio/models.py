from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Projeto(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.CharField(max_length=250)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='templates/portfolio/img')

    def __str__(self):
        return self.titulo