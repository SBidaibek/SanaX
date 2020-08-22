from django.urls import path
from .api.student import get_student_info, get_student_course_list, get_student_choice_list, create_choice


urlpatterns = [
    path('get_student_info/', get_student_info),
    path('get_student_course_list/', get_student_course_list),
    path('get_student_choice_list/', get_student_choice_list),
    path('create_choice/', create_choice),
]
