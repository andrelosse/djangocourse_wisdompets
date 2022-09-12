from django.db import models

class Pets(models.Model):

    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=57)
    breed = models.CharField(max_length=57)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    age = models.IntegerField(null=True)
    submission_date = models.DateTimeField()
    description = models.TextField()
    vaccinations = models.ManyToManyField('Vaccines', blank=True)

class Vaccines(models.Model):

    name = models.CharField(max_length=57)

    def __str__ (self):
        return self.name
