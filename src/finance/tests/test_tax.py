import json
from django.test import TestCase

from src.finance.models import *
from utils.helpers import *
from src.account.models import Staff, StaffUser
from utils.base_test import *


class TaxInformationTestCase(TestCase):
    def setUp(self):
        create_test_user(StaffUser)
        create_staff(Staff)

        self.staff = Staff.objects.first()

        _tax = TaxInformation.objects.create(
            deductions=500.00,
            exemptions=300,
            staff=self.staff,
            tax_bracket='Payee'
        )
        _tax.save()

        self.tax = TaxInformation.objects.first()

    def test_tax_created(self):
        self.assertTrue(self.tax.pk == 1)
        self.assertTrue(self.tax.exemptions == 300)

    def test_tax_post(self):
        data = {
            "deductions": 200.00,
            "exemptions": 150,
            "tax_bracket": "PAYEE",
            "staff": {
                "staffId": self.staff.staff_id,
                "firstName": self.staff.first_name,
                "middleName": self.staff.middle_name,
                "lastName": self.staff.last_name,
                "phoneNumber": self.staff.phone_number,
                "dateOfBirth": self.staff.date_of_birth
            }
        }
        req = self.client.post('/api/tax-information/',
                               data=data, content_type='application/json', **add_headers())
        self.assertTrue(req.status_code == 201)

    def test_tax_get(self):
        _req = self.client.get('/api/tax-information/', **add_headers())
        self.assertTrue(_req.status_code == 200)

    def test_tax_put(self):
        _req = self.client.get('/api/tax-information/1/', **add_headers())
        obj = _req.json()

        data = {
            "id": 1,
            "deductions": obj['deductions'],
            "exemptions": 100,
            "taxBracket": obj.get('taxBracket'),
            "staff": obj['staff']
        }

        req = self.client.put('/api/tax-information/1/',
                              data=data, content_type='application/json', **add_headers())
        self.assertEqual(req.status_code, 200)

    def test_tax_delete(self):
        _req = self.client.delete('/api/tax-information/1/', **add_headers())
        self.assertEqual(_req.status_code, 204)
