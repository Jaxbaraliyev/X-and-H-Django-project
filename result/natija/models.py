from django.db import models


class Togri(models.Model):
    soz = models.CharField(max_length=20)

    def __str__(self):
        return self.soz


class Notogri(models.Model):
    soz = models.CharField(max_length=20)
    togri = models.ForeignKey(Togri, on_delete=models.CASCADE)


    def __str__(self):
        return self.soz