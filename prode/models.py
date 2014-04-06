#coding=UTF-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50, verbose_name='nombre')
    flag_image = ImageField(_(u'bandera'), upload_to='img/flags')

    def __unicode__(self):
        return self.name

    class Meta:
            verbose_name = u"Selección"
            verbose_name_plural = u"Selecciones"

class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name='nombre')
    logo = ImageField(_(u'logo'), upload_to='img/logos')

    def __unicode__(self):
        return self.name

    class Meta:
            verbose_name = u"Empresa"

class Department(models.Model):
    name = models.CharField(max_length=50, verbose_name='nombre')
    company = models.ForeignKey(Company, verbose_name=u'empresa')

    def __unicode__(self):
        return self.name

    class Meta:
            verbose_name = u"Departamento"

class Phase(models.Model):
    name = models.CharField(max_length=50, verbose_name='nombre')
    start_date = models.DateField('fecha de inicio')
    finish_date = models.DateField(verbose_name='fecha de cierre')

    def __unicode__(self):
        return self.name

    class Meta:
            verbose_name = u"Fase"

class Match(models.Model):
    GOALS_CHOICES = []
    for i in range (0, 20):
        GOALS_CHOICES.insert(0,(i, i))

    first_team = models.ForeignKey(Team, verbose_name='Equipo 1', related_name='match_first_team')
    second_team = models.ForeignKey(Team, verbose_name='Equipo 2', related_name='match_second_team')
    phase = models.ForeignKey(Phase, verbose_name='Fase')
    date = models.DateField('horario de inicio')
    start_datetime = models.TimeField('horario de inicio')
    first_team_goals = models.PositiveIntegerField(choices=GOALS_CHOICES, null=True, blank=True)
    second_team_goals = models.PositiveIntegerField(choices=GOALS_CHOICES, null=True, blank=True)

    def __unicode__(self):
        return u'%s VS %s - %s' % (self.first_team, self.second_team, self.date.strftime('%d/%m'))

    class Meta:
            verbose_name = u"Partido"