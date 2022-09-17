from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SeminarHall(models.Model):
    hallid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    wifi = models.BooleanField()
    projector = models.BooleanField()
    speaker = models.BooleanField()
    microphone = models.BooleanField()
    camera = models.BooleanField()
    ac = models.BooleanField()
    Location = models.CharField(max_length=50)
    Rating = models.IntegerField()

    def __str__(self):
        return self.name


class Request(models.Model):
    reqid = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hall = models.ForeignKey(SeminarHall, on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    reason = models.TextField()
    poster = models.ImageField(upload_to='posters/', blank=True)
    permLetter = models.FileField(upload_to='permissionLetters/', blank=True)
    status = models.CharField(max_length=50, default='pending')

    def __str__(self):
        return self.reqid


class AllotedHall(models.Model):
    allotid = models.AutoField(primary_key=True)
    hallRequest = models.ForeignKey(Request, on_delete=models.CASCADE)
    hall = models.ForeignKey(SeminarHall, on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

    def __str__(self):
        return self.allotid


class Feedback(models.Model):
    fbid = models.AutoField(primary_key=True)
    allotment = models.ForeignKey(AllotedHall, on_delete=models.CASCADE)
    facAvialed = models.IntegerField()
    cleanliness = models.IntegerField()
    remarkd = models.TextField()

    def __str__(self):
        return self.fbid


