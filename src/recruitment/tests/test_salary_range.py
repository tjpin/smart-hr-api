from django.test import TestCase

from src.recruitment.models import *
from utils.base_test import *
from src.account.models import StaffUser


class CandidateTestCase(TestCase):
    def setUp(self):
        create_test_user(StaffUser)
        _range = SalaryRange.objects.create(salary_range="2500 - 5000")
        _range.save()

        self.salary_range = SalaryRange.objects.first()

    def test_object_created(self):
        self.assertTrue(self.salary_range.pk == 1)
        self.assertTrue(self.salary_range.salary_range == "2500 - 5000")

    def test_salary_range_post(self):
        data = {"salary_range": "2500 - 5000"}
        req = self.client.post(
            '/api/recruitment/salary-range/', data=data, **add_headers(), content_type="application/json")
        self.assertTrue(req.status_code == 201)

    def test_salary_range_put(self):
        data = {"salary_range": "2000 - 3000"}
        req = self.client.put(
            '/api/recruitment/salary-range/1/', data=data, **add_headers(), content_type="application/json")

        self.assertTrue(req.status_code == 200)
        self.assertTrue(req.json()["salaryRange"] == "2000 - 3000")

    def test_salary_range_get(self):
        req = self.client.get(
            '/api/recruitment/salary-range/', **add_headers())
        _req = self.client.get(
            '/api/recruitment/salary-range/1/', **add_headers())

        data = req.json()
        _data = _req.json()

        self.assertTrue(req.status_code == 200)
        self.assertTrue(_req.status_code == 200)

        self.assertEqual(data[0]['salaryRange'], _data['salaryRange'])

    def test_salary_range_delete(self):
        req = self.client.delete(
            '/api/recruitment/salary-range/1/', **add_headers())
        _req = self.client.get(
            '/api/recruitment/salary-range/1/', **add_headers())
        self.assertTrue(req.status_code == 204)
        self.assertTrue(_req.status_code == 404)
