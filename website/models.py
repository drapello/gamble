from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return '%s' % (self.username)

class Projeto(models.Model):
    nome = models.CharField(max_length=255, null=True, blank=True)
    linguagem = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.nome, self.linguagem)
        
class Profile(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    linguagens = models.CharField(max_length=255, null=True, blank=True)
    projetos = models.IntegerField(null=True, blank=True)
    contactado = models.NullBooleanField(null=True, blank=True)
    iniciado = models.NullBooleanField(null=True, blank=True)
    aprovado = models.NullBooleanField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    #projetos = models.ManyToManyField(Projeto, related_name='projetos')

    def __str__(self):
        return '%s' % (self.username)
