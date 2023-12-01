import json

from django.test import TestCase

from src.finance.models import Benefit
from utils.base_test import *
from src.account.models import StaffUser, Staff


class BenefitTestCase(TestCase):
    def setUp(self):
        create_test_user(StaffUser)
        create_staff(Staff)

        self.staff = Staff.objects.first()

        _benefit = Benefit.objects.create(
            benefit_name="Yearly bonus",
            benefit_type="Appreciation",
            contribution_amount=100.00,
            staff=self.staff
        )
        _benefit.save()

        self.benefit = Benefit.objects.first()

    def test_benefit_create(self):
        self.assertTrue(self.benefit.pk == 1)

    def test_benefit_auth(self):
        req = self.client.get('/api/benefits/')
        self.assertTrue(req.status_code == 401)  # unauthorized

    def test_benefit_get(self):
        req = self.client.get('/api/benefits/', **add_headers())
        self.assertTrue(req.status_code == 200)

    def test_benefit_post(self):
        data = {
            "benefitName": "bonus",
            "benefitType": "Gift",
            "contributionAmount": 50.00,
            "staff": self.staff.pk
        }
        req = self.client.post('/api/benefits/', data=data, **add_headers())
        self.assertTrue(req.status_code == 201)
