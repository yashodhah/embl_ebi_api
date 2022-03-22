from django.db import models


class Molecule(models.Model):
    name = models.CharField(max_length=50)
    max_phase = models.IntegerField()
    structure = models.CharField(max_length=4000)
    inchi_key = models.CharField(max_length=27)

    class Meta:
        db_table = "molecule"


class Target(models.Model):
    name = models.CharField(max_length=100)
    organism = models.CharField(max_length=100)

    class Meta:
        db_table = "target"


class Activity(models.Model):
    type = models.CharField(max_length=250)
    units = models.CharField(max_length=100)
    value = models.FloatField()
    relation = models.CharField(max_length=2)
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    molecule = models.ForeignKey(Molecule, on_delete=models.CASCADE)

    class Meta:
        db_table = "activity"
