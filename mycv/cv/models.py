from django.db import models
from django.utils import timezone

class PersonalData(models.Model):
    name = models.CharField('Nome',max_length=120)
    address = models.CharField('Endereco', max_length=150)
    email = models.EmailField('Email', max_length=120)
    phone  = models.CharField('Telefone', max_length=80)
    url_Linkedin = models.URLField('LinkedIn', max_length=80)
    age = models.IntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Objective(models.Model):
    description = models.CharField('Objetivo', max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.description

class ProfessionalExperience(models.Model):
    company = models.CharField('Empresa', max_length=150)
    post = models.CharField('Cargo', max_length=80)
    location = models.CharField('Local', max_length=80)
    period = models.CharField('Periodo', max_length=80)
    description = models.TextField('Descricao')

    def publish(self):
        self.save()

    def __str__(self):
        return self.company

class Education(models.Model):
    campus = models.CharField('Escola', max_length=150)
    course = models.CharField('Curso', max_length=150)
    location = models.CharField('Local', max_length=80)
    period = models.CharField('Periodo', max_length=80)
    description = models.TextField('Descricao')

    def publish(self):
        self.save()

    def __str__(self):
        return self.campus

class Skill(models.Model):
    description = models.TextField('Descricao')

    def publish(self):
        self.save()

    def __str__(self):
        return self.description

class Language(models.Model):
    name = models.CharField('Nome', max_length=150)
    Idiom = models.CharField('Idioma', max_length=80)
    period = models.CharField('Periodo', max_length=80)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Certificate(models.Model):
    description = models.TextField('Descricao')

    def publish(self):
        self.save()

    def __str__(self):
        return self.description




class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

