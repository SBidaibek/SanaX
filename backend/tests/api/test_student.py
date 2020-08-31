from django.test import TestCase, Client

from rest_framework import status

from parameterized import parameterized

from backend.models import User, Student, Teacher, Choice, Material, Course
from backend.models import EducationLevel, Subject, Language


class TestStudent(TestCase):

    STUDENT_USERNAME = 'test_student'
    STUDENT_PASSWORD = 'test_student_password'
    STUDENT_EMAIL = 'student@mail.test'

    TEACHER_USERNAME = 'test_teacher'
    TEACHER_PASSWORD = 'test_teacher_password'
    TEACHER_EMAIL = 'teacher@mail.test'

    COURSE_NUMBER = 3

    CHOICE_SUBJECTS = [Subject.Mathematics,
                       Subject.Mathematics, Subject.Mathematics]
    CHOICE_LANGUAGES = [Language.Russian, Language.Kazakh, Language.English]
    CHOICE_DIFFICULTIES = [20, 50, 5]
    CHOICE_LOWEST_PRICES = [10, 1, 30]
    CHOICE_HIGHEST_PRICES = [20, 25, 100]
    CHOICE_PERSONAL_LESSON_PREFERENCES = [False, True, False]
    CHOICE_DURATIONS = ['01:30:00', '00:45:30', '02:00:00']

    MATERIAL_SUBJECTS = [Subject.Mathematics,
                         Subject.Mathematics, Subject.Mathematics]
    MATERIAL_LANGUAGES = [Language.Russian, Language.Kazakh, Language.English]
    MATERIAL_DIFFICULTIES = [15, 60, 12]
    MATERIAL_PRICES = [12, 5, 40]
    MATERIAL_DURATIONS = ['01:15:00', '01:00:00', '01:30:30']

    COURSE_NAMES = ["Test Course 1", "Second TEST Course",
                    "Introductions to Test Course 3"]
    COURSE_DESCRIPTIONS = ["Description 1", "Description 2", "Description 3"]
    COURSE_PROGRESS = [0, 45, 99]

    def setUp(self):
        self.student_user = User.objects.create(
            username=self.STUDENT_USERNAME,
            password=self.STUDENT_PASSWORD,
            email=self.STUDENT_EMAIL,
        )
        self.student = Student.objects.create(
            user=self.student_user, edu_level=EducationLevel.Middle
        )

        self.teacher_user = User.objects.create(
            username=self.TEACHER_USERNAME,
            password=self.TEACHER_PASSWORD,
            email=self.TEACHER_EMAIL,
        )
        self.teacher = Teacher.objects.create(
            user=self.teacher_user,
            bio='Test Bio of the test Teacher',
            subject=Subject.Mathematics,
            language=Language.Kazakh,
        )

        self.choices = []
        for i in range(self.COURSE_NUMBER):
            self.choices.append(Choice.objects.create(
                subject=self.CHOICE_SUBJECTS[i],
                student=self.student,
                language=self.CHOICE_LANGUAGES[i],
                difficulty=self.CHOICE_DIFFICULTIES[i],
                preferredLowestPrice=self.CHOICE_LOWEST_PRICES[i],
                preferredHighestPrice=self.CHOICE_HIGHEST_PRICES[i],
                preferPersonalLessons=self.CHOICE_PERSONAL_LESSON_PREFERENCES[i],
                preferredDuration=self.CHOICE_DURATIONS[i],
            ))

        self.materials = []
        for i in range(self.COURSE_NUMBER):
            self.materials.append(Material.objects.create(
                creator=self.teacher,
                subject=self.MATERIAL_SUBJECTS[i],
                language=self.MATERIAL_LANGUAGES[i],
                difficulty=self.MATERIAL_DIFFICULTIES[i],
                price=self.MATERIAL_PRICES[i],
                duration=self.MATERIAL_DURATIONS[i],
            ))

        self.courses = []
        for i in range(self.COURSE_NUMBER):
            self.courses.append(Course.objects.create(
                material=self.materials[i],
                choice=self.choices[i],
                name=self.COURSE_NAMES[i],
                description=self.COURSE_DESCRIPTIONS[i],
                progress=self.COURSE_PROGRESS[i],
            ))

    @parameterized.expand([
        (EducationLevel.Low, ),
        (EducationLevel.Middle, ),
        (EducationLevel.High, ),
    ])
    def test_get_student_info(self, edu_level):
        self.student.edu_level = edu_level
        self.student.save()

        c = Client()
        data = {'id': self.student_user.id}
        response = c.post('/api/get_student_info/', data,
                          content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('id', response.data)
        self.assertEqual(response.data['id'], self.student_user.id)

        self.assertIn('edu_level', response.data)
        self.assertEqual(response.data['edu_level'], edu_level)

    def test_get_student_choice_list_fields(self):
        for i in range(1, self.COURSE_NUMBER):
            self.choices[i].delete()

        choice = self.choices[0]

        c = Client()
        data = {'id': self.student_user.id}
        response = c.post('/api/get_student_choice_list/',
                          data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        choice_data = response.data[0]

        fields = (
            'id',
            'subject',
            'language',
            'difficulty',
            'preferredLowestPrice',
            'preferredHighestPrice',
            'preferPersonalLessons',
            'preferredDuration',
        )
        self.assertEqual(len(choice_data), len(fields))

        for field_name in fields:
            self.assertIn(field_name, choice_data)
            self.assertEqual(choice_data[field_name],
                             getattr(choice, field_name))

    def test_get_student_choice_list_on_multiple_choices(self):
        c = Client()
        data = {'id': self.student_user.id}
        response = c.post('/api/get_student_choice_list/',
                          data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.COURSE_NUMBER)

        choice_ids = [choice_data['id'] for choice_data in response.data]
        for choice in self.choices:
            self.assertIn(choice.id, choice_ids)

    def test_get_student_course_list_fields(self):
        for i in range(1, self.COURSE_NUMBER):
            self.courses[i].delete()

        course = self.courses[0]

        c = Client()
        data = {'id': self.student_user.id}
        response = c.post('/api/get_student_course_list/',
                          data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        course_data = response.data[0]

        fields = (
            'id',
            'name',
            'description',
            'progress',
        )
        self.assertEqual(len(course_data), len(fields))

        for field_name in fields:
            self.assertIn(field_name, course_data)
            self.assertEqual(course_data[field_name],
                             getattr(course, field_name))

    def test_get_student_course_list_on_multiple_courses(self):
        c = Client()
        data = {'id': self.student_user.id}
        response = c.post('/api/get_student_course_list/',
                          data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.COURSE_NUMBER)

        course_ids = [course_data['id'] for course_data in response.data]
        for course in self.courses:
            self.assertIn(course.id, course_ids)

    @parameterized.expand([
        (Subject.Mathematics, Language.Kazakh, 50,
         100, 200, True, '02:30:15', status.HTTP_200_OK),
        (Subject.Mathematics, Language.Kazakh, 50,
         100, 200, True, 'two hours', status.HTTP_400_BAD_REQUEST),
        (Subject.Mathematics, Language.Kazakh, 50,
         500, 1, True, '02:30:15', status.HTTP_500_INTERNAL_SERVER_ERROR),
    ])
    def test_create_choice(self, subject, language, difficulty, lowest_price, highest_price, personal, duration, expected_status_code):
        data = {
            'id': self.student_user.id,
            'subject': subject,
            'language': language,
            'difficulty': difficulty,
            'preferredLowestPrice': lowest_price,
            'preferredHighestPrice': highest_price,
            'preferPersonalLessons': personal,
            'preferredDuration': duration,
        }

        c = Client()
        response = c.post('/api/create_choice/', data,
                          content_type='application/json')

        self.assertEqual(response.status_code, expected_status_code)

        if response.status_code == status.HTTP_200_OK:
            self.assertIn('id', response.data)
            choice = Choice.objects.get(id=response.data['id'])

            data.pop('id')
            for key, val in data.items():
                self.assertEqual(str(val), str(getattr(choice, key)),
                                 'key={}'.format(key))
