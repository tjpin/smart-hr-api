from django.test import TestCase

from src.finance.models import *
from utils.base_test import *
from src.account.models import StaffUser


class SalaryStructureTestCase(TestCase):
    def setUp(self):
        create_test_user(StaffUser)
        _structure = SalaryStructure.objects.create(
            structure_name="Monthly",
            allowances=200.00,
            basic_pay=2000.00,
            bonus=200.00,
            deductions=0.00
        )
        _structure.save()

        self.structure = SalaryStructure.objects.first()

    def test_structure_created(self):
        self.assertTrue(self.structure.pk == 1)
        self.assertTrue(self.structure.deductions == 0.00)

    def test_structure_post(self):
        data = {
            "structure_name": "Monthly",
            "allowances": 200.00,
            "basic_pay": 2000.00,
            "bonus": 200.00,
            "deductions": 0.00
        }
        req = self.client.post('/api/salary-structures/',
                               data=data, **add_headers(), content_type='application/json')
        self.assertTrue(req.status_code == 201)

    def test_structure_get(self):
        req = self.client.get('/api/salary-structures/', **add_headers())
        _req = self.client.get('/api/salary-structures/1/', **add_headers())
        data = _req.json()

        self.assertEqual(req.status_code, 200)
        self.assertEqual(_req.status_code, 200)
        self.assertTrue(data['allowances'] == "200.00")
        self.assertTrue(data['structureName'] == "Monthly")

    def test_structure_put(self):
        _req = self.client.get('/api/salary-structures/1/', **add_headers())
        _data = _req.json()
        data = {
            "structureName": _data['structureName'],
            "allowances": 500.00,
            "basicPay": 3000.00,
            "bonus": 0.00,
            "deductions": 100.00
        }
        req = self.client.put('/api/salary-structures/1/',
                              data=data, **add_headers(), content_type='application/json')
        _st = self.client.get('/api/salary-structures/1/', **add_headers())
        _st_data = _st.json()

        self.assertTrue(req.status_code == 200)
        self.assertTrue(_st_data['allowances'] == "500.00")
        self.assertTrue(_st_data['basicPay'] == "3000.00")

    def test_structure_delete(self):
        req = self.client.delete('/api/salary-structures/1/', **add_headers())
        self.assertTrue(req.status_code == 204)
