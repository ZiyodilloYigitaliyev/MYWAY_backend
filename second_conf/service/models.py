from django.db import models
from django.contrib.auth.models import User

#---------- Manzillar ------------------------#
class ServiceAddres(models.Model):
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    location = models.CharField(max_length=250)

#---------- Texnik Ko'rik -----------------#
class TexServiceOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Bog'langan foydalanuvchi
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    avtoNum = models.CharField(max_length=50)
    Date = models.DateField()
    region = models.CharField(max_length=50)
    myService = models.CharField(max_length=150)
    locations = models.ForeignKey(ServiceAddres, on_delete=models.CASCADE)


# ------------ Gas --------------------#
class Gas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Bog'langan foydalanuvchi
    name = models.CharField(max_length=150)
    startDate = models.DateField()
    endDate = models.DateField()
    testDate = models.DateField()

#---------------- Car oil  ---------------#
class CarOil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Bog'langan foydalanuvchi
    startDate = models.DateField()
    traveled = models.IntegerField(150)
    brand = models.CharField(max_length=150)
    recommendedKm = models.IntegerField(150)
    dailyKm = models.IntegerField(150)
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

#---------------- Texnik xizmat ko'rsatish  --------------------#
class TexServiceMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Bog'langan foydalanuvchi
    email = models.EmailField(max_length=150)
    phoneNum = models.CharField(max_length=13)
    event = models.CharField(max_length=250)
    def __str__(self):
        return self.email

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


#-------- Ma’muriy amaliyot bo’limi --------------------------#
class Department(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Bog'langan foydalanuvchi
    fName = models.CharField(max_length=150)
    departmentName = models.CharField(max_length=150)
    departmentHead = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phoneNum = models.CharField(max_length=13)

