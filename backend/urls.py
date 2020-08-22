from django.urls import path, include
from .api.student import get_student_info, get_student_course_list, get_student_choice_list, create_choice

from knox.views import LogoutView

from .views import UserAPIView, RegisterAPIView, LoginAPIView

urlpatterns = [
    path('', include('knox.urls')),
    path('user', UserAPIView.as_view()),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutView.as_view(), name='knox_logout'),
    path('get_student_info/', get_student_info),
    path('get_student_course_list/', get_student_course_list),
    path('get_student_choice_list/', get_student_choice_list),
    path('create_choice/', create_choice),
]