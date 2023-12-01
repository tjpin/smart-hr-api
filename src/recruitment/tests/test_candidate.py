from django.test import TestCase

from src.recruitment.models import *
from utils.base_test import *
from src.account.models import StaffUser


class CandidateTestCase(TestCase):
    def setUp(self):
        create_test_user(StaffUser)

        _candidate = Candidate.objects.create(
            first_name="Test",
            last_name="User",
            phone=123456789
        )
        _candidate.save()

        self.candidate = Candidate.objects.first()

    def test_object_created(self):
        self.assertTrue(self.candidate.pk == 1)
        self.assertTrue(self.candidate.phone == "123456789")

    def test_candidate_post(self):
        data = {
            "first_name": "Test",
            "last_name": "User",
            "phone": "123456981"
        }
        req = self.client.post(
            '/api/recruitment/candidates/', data=data, **add_headers())
        self.assertTrue(req.status_code == 201)

    def test_candidate_put(self):
        _req = self.client.get('/api/recruitment/candidates/1/')
        data = {
            "first_name": "New",
            "last_name": _req.json()['lastName'],
            "phone": "20006654"
        }
        req = self.client.put(
            '/api/recruitment/candidates/1/', data=data, **add_headers(), content_type='application/json')

        _data = self.client.get('/api/recruitment/candidates/1/')

        self.assertTrue(req.status_code == 200)
        self.assertEqual(_data.json()['firstName'], "New")
        self.assertEqual(_data.json()['phone'], "20006654")

    def test_candidate_get(self):
        req = self.client.get('/api/recruitment/candidates/', **add_headers())
        _req = self.client.get(
            '/api/recruitment/candidates/1/', **add_headers())

        self.assertEqual(req.json()[0]['firstName'], _req.json()['firstName'])
        self.assertEqual(req.json()[0]['lastName'], _req.json()['lastName'])
        self.assertEqual(req.json()[0]['phone'], _req.json()['phone'])

    def test_candidate_delete(self):
        req = self.client.delete(
            '/api/recruitment/candidates/1/', **add_headers())
        _req = self.client.get(
            '/api/recruitment/candidates/1/', **add_headers())

        self.assertEqual(req.status_code, 204)
        self.assertEqual(_req.status_code, 404)
