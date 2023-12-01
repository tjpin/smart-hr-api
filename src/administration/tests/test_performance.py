from django.test import TestCase
from datetime import datetime as dt

from src.administration.models import *
from src.account.models import Staff, StaffUser
from utils.base_test import (create_test_user, add_headers, random_staffs)

class PerformanceTestCase(TestCase):
    def setUp(self):
        create_test_user(StaffUser)
        _staff = Staff.objects.create(
            staff_id='1098016210675964',
            first_name='Jane',
            middle_name="Mills",
            last_name="Doe",
            date_of_birth=timezone.now().strftime('%Y-%m-%d'),
            phone_number=10345689
        ).save()
        _reviewer = Staff.objects.create(
            staff_id='1098016210675963',
            first_name='Johh',
            middle_name="Jay",
            last_name="Kahn",
            date_of_birth=timezone.now().strftime('%Y-%m-%d'),
            phone_number=12445689
        ).save()
        self.staff = Staff.objects.first()
        self.reviewer = Staff.objects.last()

        performance = PerformanceReview.objects.create(
            staff=self.staff,
            rating=4,
            reviewer=self.reviewer,
            review_date=dt(2023, 5, 12).date(),
            feedback="Improved"
        )

        self.performance = PerformanceReview.objects.filter(
            staff__staff_id=self.staff.staff_id)

    def test_performance_created(self):
        self.assertTrue(self.performance.exists())

    def test_performance_post(self):
        data = {
            "staff": self.staff.pk,
            "rating": 4,
            "reviewer": self.reviewer.pk,
            "reviewDate": dt(2023, 5, 12).date(),
            "feedback": "Improved"
        }
        response = self.client.post('/api/performance-reviews/', data=data,
                                    content_type='application/json', **add_headers())
        perf = response.json()
        self.assertTrue(response.status_code == 201)
        self.assertEqual(perf["staff"], self.staff.staff_id)
        self.assertEqual(perf["reviewer"], self.reviewer.staff_id)

    def test_performance_put(self):
        _perf = self.client.get('/api/performance-reviews/1/', **add_headers())
        perf = _perf.json()
        data = {
            "staff": perf['staff'],
            "rating": 0,
            "reviewer": perf['reviewer'],
            "reviewDate": "2023-08-12",
            "feedback": "Improved"
        }
        response = self.client.put('/api/performance-reviews/1/', data=data,
                                   content_type='application/json', **add_headers())
        _response = response.json()
        self.assertTrue(response.status_code == 200)
        self.assertTrue(_response["reviewDate"] == "2023-08-12")

    def test_performance_delete(self):
        response = self.client.delete('/api/performance-reviews/1/', **add_headers())
        self.assertEqual(response.status_code, 204)
        _response = self.client.get('/api/performance-reviews/1/', **add_headers())
        self.assertTrue(_response.status_code == 404)
