from django.db import models

# Create your models here.
class Patients(models.Model):
    flag = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    patient_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    class Meta:
        unique_together = ('date','patient_id')
    def __str__(self):
        return self.date
