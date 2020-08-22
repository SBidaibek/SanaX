from rest_framework import serializers

from .models import Student, Course, Choice


class StudentSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)

    def get_id(self, student):
        return student.user.id if student.user is not None else 0 

    class Meta:
        model = Student
        fields = ['id', 'edu_level']

        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'progress']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'subject', 'language', 'difficulty', 'preferredLowestPrice', 'preferredHighestPrice', 'preferPersonalLessons', 'preferredDuration']
