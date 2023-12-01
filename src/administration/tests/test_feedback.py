from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from src.account.models import Staff, StaffUser
from src.administration.engagement import *
from utils.base_test import (create_test_user, add_headers, random_staffs)


class EngagementTestCase(TestCase):
    def setUp(self):
        create_test_user(StaffUser)
        _staff = Staff.objects.create(
            staff_id='1098016210675962',
            first_name='Jane',
            middle_name="Mills",
            last_name="Doe",
            date_of_birth=timezone.now().strftime('%Y-%m-%d'),
            phone_number=12345689
        ).save()
        self.staff = Staff.objects.first()

        _feedback = FeedBack.objects.create(
            date=timezone.now().strftime('%Y-%m-%d'),
            staff=self.staff,
            feedback="I love the new programe"
        )
        _feedback.save()
        self.feedback = FeedBack.objects.first()
        # self.baseUrl = "/api"

    def test_feedback_created(self):
        self.assertTrue(self.feedback.pk == 1)

    def test_feedback_post(self):

        data = {
            "staff": self.staff.pk,
            "feedback": "I love the new programe",
            "date": "2023-08-22"
        }
        req = self.client.post('/api/feedbacks/', data=data, **add_headers())
        self.assertTrue(req.status_code == 201)

    def test_feedback_put(self):
        _req = self.client.get('/api/feedbacks/1/', **add_headers())
        jsonData = _req.json()
        data = {
            "staff": jsonData["staff"]["staffId"],
            "feedback": "updated",
            "date": jsonData["date"],
        }
        req = self.client.put('/api/feedbacks/1/', data=data,
                              **add_headers(), content_type="application/json")
        updateData = req.json()
        self.assertTrue(req.status_code == 200)
        self.assertEqual(updateData["feedback"], "updated")

    def test_feedback_delete(self):
        req = self.client.delete('/api/feedbacks/1/', **add_headers())
        self.assertEqual(req.status_code, 204)


