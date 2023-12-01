import json

from django.contrib.auth.hashers import check_password
from django.test import TestCase
from datetime import datetime as dt

from .models import *
from src.account.staff import *
from src.account.models import StaffUser
from utils.base_test import (create_test_user, add_headers, random_staffs)


class AccountsTestCase(TestCase):
    def setUp(self):
        create_test_user(StaffUser)
        random_staffs(Staff, Department)

        self.dpt1 = Department.objects.get(department_name="Administration")
        self.staffs = Staff.objects.all()

    def test_login(self):
        data = {"username": 31567970, "password": "admin.123"}
        req = self.client.post('/admin/', data=data, **
                               add_headers(), content_type="application/json")
        self.assertRedirects(
            req, '/admin/login/?next=/admin/', status_code=302)

    def test_staff_create(self):
        staff = Staff.objects.filter(department=1)
        users = StaffUser.objects.filter(staff=self.staffs.first())
        _user = users.first()
        password = users.first().password
        self.assertTrue(check_password(
            f"{_user.staff.last_name}_{_user.staff.phone_number}".lower(), password))
        self.assertTrue(users.exists())
        self.assertTrue(staff.exists(), True)
        self.assertTrue(staff.first().first_name, 'Test')
        self.assertTrue(staff.first().phone_number == 12345678)
        self.assertEqual(staff.count(), 10)

    # ''' API CRUD tests '''

    def test_user_post(self):
        staff = Staff.objects.first()
        data = {
            "phoneNumber": 2200335588,
            "staff": {
                "phoneNumber": staff.phone_number,
                "firstName": staff.first_name,
                "middleName": staff.middle_name,
                "lastName": staff.last_name,
                "dateOfBirth": f"{dt.now().strftime('%Y-%m-%d')}"
            }
        }
        request = self.client.post(
            '/api/users/', data=data, content_type='application/json', **add_headers())
        self.assertTrue(request.status_code == 201)

    def test_api_connection(self):
        request1 = self.client.get('/api/', **add_headers())
        self.assertTrue(request1.status_code == 200)

        request2 = self.client.get('/api/v1/', **add_headers())
        self.assertFalse(request2.status_code == 200)
        self.assertTrue(request2.status_code == 404)

        request3 = self.client.get('/api/users/', **add_headers())
        self.assertTrue(request3.status_code == 200)

        request4 = self.client.get('/api/payroll-records/', **add_headers())
        self.assertTrue(request4.status_code == 200)

    def test_department_get(self):
        req = self.client.get('/api/departments/', **add_headers())
        self.assertTrue(req.status_code == 200)

    def test_staff_post(self):
        data = {
            "department_name": "Events"
        }
        dept = self.client.post('/api/departments/',
                                data=data, content_type='application/json', **add_headers())
        self.assertTrue(dept.status_code == 201)

        staff = {
            "staffId": '10',
            "firstName": "Test",
            "middleName": "Middle",
            "lastName": "Last",
            "dateOfBirth": "1997-03-22",
            "gender": "Not Specified",
            "phoneNumber": 115807698,
            "joiningDate": f"{dt.now().strftime('%Y-%m-%d')}"
        }
        new_staff = self.client.post(
            '/api/staffs/', data=staff, content_type='application/json', **add_headers())
        self.assertEqual(new_staff.status_code, 201)

    def test_staff_put(self):
        _req = self.client.get('/api/staffs/1/', **add_headers())
        _staff = _req.json()
        staff = {
            "staffId": _staff['staffId'],
            "firstName": _staff['firstName'],
            "middleName": _staff['middleName'],
            "lastName": "Updated",
            "dateOfBirth": _staff['dateOfBirth'],
            "department": _staff['department'],
            "grade": _staff['grade'],
            "gender": "Male",
            "phoneNumber": _staff['phoneNumber'],
            "joiningDate": _staff['joiningDate']
        }
        req = self.client.put('/api/staffs/1/', data=staff,
                              content_type='application/json', **add_headers())

        self.assertTrue(req.status_code == 200)

    def test_staff_delete(self):
        _req = self.client.delete('/api/staffs/1/', **add_headers())
        self.assertEqual(_req.status_code, 204)
