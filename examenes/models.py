from django.db import models
from pacientes.models import Paciente

class Examen(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default=None)
    value = models.FloatField(null=True, blank=True, default=None)
    unit = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)