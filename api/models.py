from django.db import models

class BasicInfo(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

class WheelSpecification(models.Model):
    form_number = models.CharField(max_length=100)
    submitted_by = models.CharField(max_length=100)
    submitted_date = models.DateField()
    fields = models.JSONField()

class BogieChecksheet(models.Model):
    form_number = models.CharField(max_length=100)
    inspection_by = models.CharField(max_length=100)
    inspection_date = models.DateField()
    bogie_details = models.JSONField()
    bogie_checksheet = models.JSONField()
    bmbc_checksheet = models.JSONField()