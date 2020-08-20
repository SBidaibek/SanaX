from django.urls import path
from .api.student import get_student_info, get_student_course_list


urlpatterns = [
    path('get_student_info/', get_student_info),
    path('get_student_course_list/', get_student_course_list),
]
