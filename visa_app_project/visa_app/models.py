from django.db import models

# Create your models here.
class VisaApplication(models.Model):
    age = models.IntegerField()
    income = models.FloatField()
    previous_travel = models.BooleanField()
    document_complete = models.BooleanField()
    visa_outcome = models.BooleanField(default=False)

    def __str__(self):
        return f"Visa Application: {self.id} - {'Approved' if self.visa_outcome else 'Rejected'}"
    

    