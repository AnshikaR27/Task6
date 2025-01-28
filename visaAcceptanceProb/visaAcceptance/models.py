# models.py
from django.db import models

class VisaApplication(models.Model):
    documents = models.BooleanField(default=False)
    visa_type = models.CharField(max_length=20, choices=[('Work', 'Work'), ('Study', 'Study'), ('Tourist', 'Tourist')])
    application_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')])

    def __str__(self):
        return f"Visa Application {self.id}"
