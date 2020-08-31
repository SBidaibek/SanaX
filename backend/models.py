from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    _meta = None


class Subject(models.IntegerChoices):
    Mathematics = 1


class Language(models.IntegerChoices):
    Russian = 1
    Kazakh = 2
    English = 3


class EducationLevel(models.IntegerChoices):
    Low = 1
    Middle = 2
    High = 3


class Days(models.IntegerChoices):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7


class Teacher(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=10000)
    subject = models.IntegerField(choices=Subject.choices)
    language = models.IntegerField(choices=Language.choices)


class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    edu_level = models.IntegerField(choices=EducationLevel.choices)


class Choice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='choices')
    subject = models.IntegerField(choices=Subject.choices, null=True)
    language = models.IntegerField(choices=Language.choices, null=True)
    difficulty = models.PositiveIntegerField(null=True)
    preferredLowestPrice = models.PositiveIntegerField(null=True)
    preferredHighestPrice = models.PositiveIntegerField(null=True)
    preferPersonalLessons = models.BooleanField(null=True)
    preferredDuration = models.TimeField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(preferredLowestPrice__lte=models.F('preferredHighestPrice')),
                name='preferredLowestPriceisLowerThanHighest',
            )
        ]


class TimeSlot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.PositiveIntegerField(choices=Days.choices)
    start = models.TimeField()
    end = models.TimeField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(start__lte=models.F('end')),
                name='endIsLaterThanStart'
            )
        ]


class Material(models.Model):
    creator = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)
    subject = models.IntegerField(choices=Subject.choices)
    language = models.IntegerField(choices=Language.choices)
    difficulty = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    duration = models.TimeField()
    date = models.DateField(auto_now=True)


class Specialization(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    experience = models.PositiveIntegerField()


class File(models.Model):
    file = models.FileField()
    material = models.ForeignKey(Material, null=True, on_delete=models.SET_NULL)


class Course(models.Model):
    material = models.OneToOneField(Material, on_delete=models.CASCADE)
    choice = models.OneToOneField(Choice, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=256, blank=True)
    progress = models.PositiveIntegerField(default=0)


class Lesson(models.Model):
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    duration = models.TimeField()
    meeting_link = models.URLField(max_length=200, null=True)
