from django.db import models

class Paciente(models.Model):
    name = models.CharField(max_length=50)
    identificacion = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return '{}'.format(self.name)

