from django.db import models

# Create your models here.

class LicenseToken(models.Model):
    serial_no = models.CharField('Serial No',max_length=256)
    access_token = models.CharField('Token', max_length=256)