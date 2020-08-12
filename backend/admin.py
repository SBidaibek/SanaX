from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(User, UserAdmin)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Choice)
admin.site.register(TimeSlot)
admin.site.register(Material)
admin.site.register(Specialization)
admin.site.register(File)
admin.site.register(Course)
admin.site.register(Lesson)

# Register your models here.
