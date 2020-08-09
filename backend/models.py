from django.contrib.postgres.fields import ArrayField
from django.db import models

class Teacher(models.Model):

class Student(models.Model):

class Choice(models.Model):

class Material(models.Model):
    files = ArrayField(
        models.FileField()
    )
    creator = models.ForeignKey(Teacher, on_delete=models.SET_NULL)
    subject = models.TextField(max_length=256)
    language = models.TextField(max_length=50)
    difficulty = models.IntegerField()
    price = models.IntegerField()
    duration = models.TimeField()
    date = models.DateField(auto_now = True)

class Course(models.Model):
    material = models.OneToOneField(Material,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=256, blank = True)
    progress = models.IntegerField(default = 0)

class Lesson(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    duration = models.TimeField()
    meeting_link = models.URLField(max_length=200)



