from django.test import TestCase
from django.db.models import Sum

from src.finance.models import *
from utils.base_test import *
from src.account.models import StaffUser


class PayrollRecordTestCase(TestCase):
    def setUp(self):
        create_test_user(StaffUser)
        create_staff(Staff)
        self.staff = Staff.objects.first()

        _payrol = PayrollRecord.objects.create(
            staff=self.staff,
            bonus=100.00,
            basic_pay=5300,
            start_date="2023-02-20",
            end_date="2023-03-01",
            month=MonthsOptions.MAY
        )
        _payrol.save()
        self.payroll = PayrollRecord.objects.first()

    def test_payroll_created(self):
        self.assertTrue(self.payroll.pk == 1)
        self.assertTrue(self.payroll.month == MonthsOptions.MAY)

    def test_payroll_post(self):
        data = {
            "staff": self.staff.pk,
            "bonus": 100.00,
            "basic_pay": 100.00,
            "start_date": "2023-02-20",
            "end_date": "2023-03-01",
            "month": "June",
            "allowances": [],
            "deductions": [],
        }
        req = self.client.post('/api/payroll-records/', data=data,
                               content_type='application/json', **add_headers())
        self.assertTrue(req.status_code == 201)

    def test_payroll_get(self):
        req = self.client.get('/api/payroll-records/', **add_headers())
        _req = self.client.get('/api/payroll-records/1/', **add_headers())
        data = _req.json()
        self.assertTrue(req.status_code == 200)
        self.assertTrue(data['staff']['staffId'] == self.staff.pk)

    def test_payroll_put(self):
        _req = self.client.get('/api/payroll-records/1/', **add_headers())
        _payrol = _req.json()

        data = {
            "staff": _payrol['staff']['staffId'],
            "basic_pay": 2500.00,
            "bonus": 200.00,
            "start_date": _payrol['startDate'],
            "month": _payrol['month'],
            "end_date": _payrol['endDate'],
            "allowances": _payrol['allowances'],
            "deductions": _payrol['deductions'],
        }
        req = self.client.put('/api/payroll-records/1/', data=data,
                              content_type='application/json', **add_headers())
        self.assertEqual(req.status_code, 200)

    def test_payroll_delete(self):
        req = self.client.delete('/api/payroll-records/1/', **add_headers())
        self.assertEqual(req.status_code, 204)
