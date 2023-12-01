from rest_framework.test import APITestCase
import json
from pprint import pprint
from datetime import datetime as dt

from src.account.models import StaffUser
from src.administration.engagement import Survey, Question
from utils.base_test import add_headers, create_test_user


class SurveyTestcase(APITestCase):
    def setUp(self):
        create_test_user(StaffUser)
        self.question = Question.objects.create(question="Will this pass?")
        self.question.save()

        _survey = Survey.objects.create(
            question=self.question,
            title="Test Survey",
            description="some test info",
            start_date="2023-07-20",
            end_date="2023-07-30",
            is_active=True
        )
        _survey.save()
        self.survey = Survey.objects.first()

    def test_survey_created(self):
        self.assertTrue(self.survey.pk == 1)
        self.assertTrue(self.survey.is_active == True)
        self.assertTrue(self.survey.end_date == dt(2023, 7, 30).date())
        self.assertTrue(self.survey.start_date.strftime(
            "%Y-%m-%d") == "2023-07-20")

    def test_survey_get(self):
        qs = self.client.get('/api/surveys/1/', **add_headers())
        data = qs.json()
        self.assertTrue(qs.status_code == 200)
        self.assertTrue(data["startDate"] == "2023-07-20")

    def test_survey_post(self):
        data = {
            "title": "test 1",
            "question": self.question.pk,
            "description": "description here",
            "start_date": "2023-07-20",
            "end_date": "2023-07-30",
            "is_active": True
        }
        qs = self.client.post('/api/surveys/', data=json.dumps(data),
                              **add_headers(), content_type="application/json")
        self.assertEqual(qs.status_code, 201)

    def test_survey_put(self):
        data = {
            "title": "test updated",
            "question": self.question.pk,
            "description": "description here",
            "start_date": "2023-06-15",
            "end_date": "2023-07-30",
            "is_active": True
        }
        qs = self.client.put('/api/surveys/1/', data=json.dumps(data),
                             **add_headers(), content_type="application/json")
        jsonData = qs.json()
        self.assertEqual(qs.status_code, 200)
        self.assertTrue(jsonData["title"] == "test updated")
        self.assertTrue(jsonData["startDate"] == "2023-06-15")

    def test_survey_delete(self):
        qs = self.client.delete('/api/surveys/1/', **add_headers())
        self.assertTrue(qs.status_code == 204)


