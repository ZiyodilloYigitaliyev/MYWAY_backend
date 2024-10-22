from django.db import models
from django.contrib.auth.models import User

#---------------- Haydovchilik guvohnomasini tiklash ----------------#
class RestoreLicense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Bog'langan foydalanuvchi
    fName = models.CharField(max_length=150)
    licenseNumber = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    phoneNum = models.CharField(max_length=13)
    def __str__(self):
        return self.fName

#---------------- Ishonchnoma  ----------------------#
class Affidavit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Bog'langan foydalanuvchi
    fName = models.CharField(max_length=150)
    guvoxnomaNum = models.IntegerField(20)
    startDate = models.DateField()
    endDate = models.DateField()
    lifeTime = models.CharField(max_length=150)
    givenName = models.CharField(max_length=150)
    pasSeria = models.CharField(max_length=2, blank=True)
    pasNum = models.IntegerField(6, blank=True)
    guvoxnoma2Num = models.IntegerField(150)

    def __str__(self):
        return self.fName

#-------- Ma’muriy amaliyot bo’limi --------------------------#
class Department(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Bog'langan foydalanuvchi
    fName = models.CharField(max_length=150)
    departmentName = models.CharField(max_length=150)
    departmentHead = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phoneNum = models.CharField(max_length=13)


