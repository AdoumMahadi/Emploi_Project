from django.db import models


# Create your models here.
class Emploi(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    date_emploi_occoupee = models.DateField('date occupée', blank=False, null=False)
    date_emploi_fixee = models.DateTimeField('date non occupée', blank=False, null=False)
    emploi_vide = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.title
