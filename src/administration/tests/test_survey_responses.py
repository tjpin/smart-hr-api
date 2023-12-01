from rest_framework.test import APITestCase
import json
from pprint import pprint
from datetime import datetime as dt

from src.account.models import StaffUser, Staff
from src.administration.engagement import Survey, Question, SurveyResponse
from utils.base_test import add_headers, create_test_user, create_staff
from api.serializers import StaffSerializer


class SurveyTestcase(APITestCase):
    def setUp(self):
        create_test_user(StaffUser)
        create_staff(Staff)
        self.question = Question.objects.create(question="Will this pass?")
        self.question.save()

        self.survey = Survey.objects.create(
            question=self.question,
            title="Test Survey",
            description="some test info",
            start_date="2023-07-20",
            end_date="2023-07-30",
            is_active=True
        )
        self.survey.save()
        self.staff = Staff.objects.first()

        self.response = SurveyResponse.objects.create(
            staff=self.staff,
            survey=self.survey,
            response="This is a response"
        )
        self.response.save()

    def test_response_created(self):
        self.assertTrue(self.response.pk == 1)

    def test_response_post(self):
        data = {
            "staff": self.staff.pk,
            "survey": self.survey.pk,
            "response": "This is a response"
        }
        req = self.client.post('/api/survey-responses/',
                               data=json.dumps(data), **add_headers(), content_type="application/json")
        jsonData = req.json()
        self.assertEqual(req.status_code, 201)
        self.assertEqual(jsonData["staff"], self.staff.pk)
        self.assertEqual(jsonData["survey"], self.survey.pk)

        _staff = StaffSerializer(self.staff).data
        self.assertTrue(_staff["staff_id"] == jsonData["staff"])

    def test_response_put(self):
        data = {
            "staff": self.staff.pk,
            "survey": self.survey.pk,
            "response": "This is updated response"
        }
        req = self.client.put('/api/survey-responses/1/',
                              data=json.dumps(data), **add_headers(), content_type="application/json")

        jsonData = req.json()
        self.assertEqual(req.status_code, 200)
        self.assertEqual(jsonData["response"], "This is updated response")
        self.assertEqual(jsonData["staff"], self.staff.staff_id)
        self.assertEqual(jsonData["survey"], self.survey.pk)

    def test_response_delete(self):
        req = self.client.delete('/api/survey-responses/1/', **add_headers())
        self.assertTrue(req.status_code == 204)
