from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from backend.models import User, Student, Course
from backend.serializers import StudentSerializer, CourseSerializer

def student_api(func):
    def wrapper(request):
        id = request.data.get('id', None)

        if id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if user.student is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        student = user.student

        return func(request, student)
    
    return wrapper

@api_view(['POST'])
@student_api
def get_student_info(request, student):
    # TODO check authentication stuff

    json_data = StudentSerializer(student).data

    return Response(data=json_data)


@api_view(['POST'])
@student_api
def get_student_course_list(request, student):
    # TODO check authentication stuff
    
    choices = student.choices.all()
    courses = [choice.course for choice in choices]

    json_data = CourseSerializer(courses, many=True).data

    return Response(data=json_data)