from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view
from backend.models import User, Student, Course, Choice
from backend.serializers import StudentSerializer, CourseSerializer, ChoiceSerializer


def student_api(func):
    def wrapper(request):
        id = request.data.get('id', None)

        if id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if not hasattr(user, 'student'):
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
    courses = []
    for choice in choices:
        if hasattr(choice, 'course'):
            courses.append(choice.course)

    json_data = CourseSerializer(courses, many=True).data

    return Response(data=json_data)


@api_view(['POST'])
@student_api
def get_student_choice_list(request, student):
    # TODO check authentication stuff

    choices = student.choices.all()

    json_data = ChoiceSerializer(choices, many=True).data

    return Response(data=json_data)


@api_view(['POST'])
@student_api
def create_choice(request, student):
    # TODO check authentication stuff

    choice_data = request.data
    choice_data.pop('id')
    choice_data['student_id'] = student.id

    serializer = ChoiceSerializer(data=choice_data)
    choice = None
    if (serializer.is_valid()):
        try:
            choice = Choice.objects.create(**choice_data)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'message': 'Something went wrong'})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'The form has been filled out incorrectly'})

    return Response(data={'message': 'Created choice', 'id': choice.id})
