from django.test import TestCase

from src.account.models import StaffUser
from utils.base_test import (create_test_user, add_headers, random_staffs)


class ModelTestCase(TestCase):
    def setUp(self):
        create_test_user(StaffUser)

    def test_api_endpoints(self):
        response = self.client.get('/api/departments/', **add_headers())
        self.assertEqual(response.status_code, 200)

        response1 = self.client.get('/api/departments/1/', **add_headers())
        self.assertEqual(response1.status_code, 404)

        response2 = self.client.get('/api/salary-structures/', **add_headers())
        self.assertEqual(response2.status_code, 200)

        response3 = self.client.get(
            '/api/salary-structures/1/', **add_headers())
        self.assertEqual(response3.status_code, 404)
