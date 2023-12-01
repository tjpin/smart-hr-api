from rest_framework.test import APITestCase
import json

from src.account.models import StaffUser
from src.administration.engagement import Question
from utils.base_test import add_headers, create_test_user


class QuestionTest(APITestCase):
    def setUp(self):
        create_test_user(StaffUser)
        _question = Question(
            question="Is is realy working?",
            yes_or_no=False
        )
        _question.save()
        self.question = Question.objects.first()

    def test_quetion_created(self):
        self.assertTrue(self.question.pk == 1)

    def test_question_post(self):
        data = {
            "question": "Is your work timing ok?",
            "yes_or_no": False
        }
        req = self.client.post('/api/questions/', data=data, **add_headers())
        self.assertEqual(req.status_code, 201)

    def test_question_put(self):
        _req = self.client.get('/api/questions/1/', **add_headers())
        _json = _req.json()

        data = {
            "question": "Question updated?",
            "yesOrNo": _json["yesOrNo"]
        }
        req = self.client.put('/api/questions/1/', data=json.dumps(data),
                              **add_headers(), content_type="application/json")
        resp = self.client.get('/api/questions/1/', **add_headers())
        self.assertEqual(req.status_code, 200)
        self.assertEqual(resp.json()["question"], "Question updated?")
        self.assertEqual(resp.json()["yesOrNo"], False)

    def test_question_delete(self):
        _req = self.client.delete('/api/questions/1/', **add_headers())
        resp = self.client.get('/api/questions/1/', **add_headers())
        self.assertTrue(_req.status_code == 204)
        self.assertTrue(resp.status_code == 404)
