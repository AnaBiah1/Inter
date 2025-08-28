from django.db import models

class Modalidade(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.TextField()
    curso = models.DecimalField(max_digits=10, decimal_places=2)
    turma = models.ForeignKey(Modalidade, related_name='alunos',on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='alunos/', blank=True, null=True)
    def __str__(self):
        return self.nome