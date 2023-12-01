from django.test import TestCase

from src.recruitment.models import *
from utils.base_test import *
from src.account.models import StaffUser


class JobPositionTestCase(TestCase):
    def setUp(self):
        create_test_user(StaffUser)

        _range = SalaryRange.objects.create(salary_range="2000 - 4000")
        _range.save()

        _dept = Department.objects.create(department_name='Operations')
        _dept.save()

        self.srange = SalaryRange.objects.first()
        self.dept = Department.objects.first()

        _position = JobPosition.objects.create(
            title='Manager',
            department=self.dept,
            description='1. Manage restaurant',
            experience_level='10 years required',
            location='Down Town Towers',
            salary_range=self.srange,
            skills='1. Management - 2. Operations',
            status=JobStatus.OPEN
        )
        _position.save()

        self.position = JobPosition.objects.first()

    def test_objects_created(self):
        self.assertTrue(self.position.pk == 1)
        self.assertTrue(self.position.department.pk == self.dept.pk)
        self.assertTrue(self.position.salary_range.pk == self.srange.pk)

    def test_position_post(self):
        data = {
            "title": "Hr Manager",
            "department": 1,
            "salaryRange": 1,
            "description": "1. Manage restaurant",
            "experienceLevel": '10 years required',
            "skills": "1. Management - 2. Operations",
        }
        req = self.client.post('/api/recruitment/job-positions/',
                               data=data, **add_headers(), content_type='application/json')

        self.assertTrue(req.status_code == 201)

    def test_position_put(self):
        _req = req = self.client.get(
            '/api/recruitment/job-positions/1/', **add_headers())
        obj = _req.json()

        data = {
            "title": "Operation Manager",
            "department": obj['department'],
            "description": obj['description'],
            "salaryRange": obj['salaryRange'],
            "experienceLevel": '5 years required',
            "skills": obj['skills'],
        }
        req = self.client.put('/api/recruitment/job-positions/1/',
                              data=data, **add_headers(), content_type='application/json')

        self.assertTrue(req.status_code == 200)

    def test_position_get(self):
        req = self.client.get(
            '/api/recruitment/job-positions/', **add_headers())
        _req = self.client.get(
            '/api/recruitment/job-positions/1/', **add_headers())

        self.assertTrue(req.status_code == 200)
        self.assertTrue(_req.json()['title'] == "Manager")
        self.assertTrue(_req.json()['experienceLevel'] == "10 years required")

    def test_position_delete(self):
        req = self.client.delete(
            '/api/recruitment/job-positions/1/', **add_headers())
        _req = self.client.get(
            '/api/recruitment/job-positions/1/', **add_headers())

        self.assertEqual(req.status_code, 204)
        self.assertEqual(_req.status_code, 404)
