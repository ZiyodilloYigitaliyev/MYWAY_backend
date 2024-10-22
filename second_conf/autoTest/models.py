from django.db import models
from django.contrib.auth.models import User

#---------------- Avtotest  results -----------------------------------#
class AutoTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Bog'langan foydalanuvchi
    trueAnswer = models.IntegerField(default=0)
    falseAnswer = models.IntegerField(default=0)
    fullAnswer = models.IntegerField(default=0)
    testID = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

#---------------- Avtotest -----------------------------------#

class AutoTestQuestionse(models.Model):
    questionID = models.AutoField(primary_key=True)
    question = models.CharField(max_length=150)
    trueAnswer = models.CharField(max_length=1)
    image = models.ImageField(upload_to='autoTest', blank=True)
    optionA = models.CharField(max_length=1)
    optionB = models.CharField(max_length=1)
    optionC = models.CharField(max_length=1)
    optionD = models.CharField(max_length=1)

