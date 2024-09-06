from django.db import models
from django.contrib.auth.models import User

class Language(models.Model):
    name = models.CharField(max_length=50)

def __str__(self):
    return self.name

class Level(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    difficulty = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.language.name} - {self.name}"

class Quiz(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
class UserMst(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=30)
    ContactNo=models.CharField(max_length=15)

    Username=models.CharField(max_length=40)

    Password=models.CharField(max_length=10)