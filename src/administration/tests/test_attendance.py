from datetime import datetime as dt
import json

from django.test import TestCase
from django.utils import timezone

from src.administration.models import *
from src.account.models import Staff, StaffUser
from utils.base_test import (create_test_user, add_headers, random_staffs)


class AttendanceTestCase(TestCase):
    def setUp(self):
        create_test_user(StaffUser)
        self.staff = Staff.objects.create(
            staff_id='1098016210675962',
            first_name='Jane',
            middle_name="Mills",
            last_name="Doe",
            date_of_birth=timezone.now().strftime('%Y-%m-%d'),
            phone_number=12345689
        )
        self.staff.save()
        attendace = Attendance.objects.create(
            staff=self.staff,
            clock_in_time=timezone.now().strftime('%H:%M:%S'),
            date=timezone.now().strftime('%Y-%m-%d')
        )
        attendace.save()

    def test_attendance_create(self):
        att = Attendance.objects.first()
        self.assertTrue(att.staff.staff_id == self.staff.staff_id)
        self.assertEqual(att.staff.phone_number, 12345689)
        # self.assertTrue(att.date == dt(2023, 7, 31).date())

    def test_attendance_post(self):
        _staff = Staff.objects.first()
        data = {
            "staff": _staff.pk,
            "clockInTime": timezone.now().strftime('%H:%M:%S'),
            "date": timezone.now().strftime('%Y-%m-%d')
        }
        req = self.client.post('/api/time-attendance/', data=data,
                               content_type="application/json", **add_headers())
        self.assertEqual(req.status_code, 201)

    def test_attendance_get(self):
        req = self.client.get('/api/time-attendance/1/', **add_headers())
        data = req.json()
        self.assertTrue(req.status_code == 200)
        self.assertEqual(data['staff'], '1098016210675962')

    def test_attendance_put(self):
        att = self.client.get('/api/time-attendance/1/', **add_headers())
        data = att.json()
        updated = {
            "staff": data.get('staff'),
            "clockInTime": data.get('clockInTime'),
            "date": "2023-04-23"
        }
        req = self.client.put('/api/time-attendance/1/',
                              data=updated, content_type="application/json", **add_headers())
        self.assertTrue(req.status_code == 200)

    def test_attendance_delete(self):
        req = self.client.delete('/api/time-attendance/1/', **add_headers())
        self.assertTrue(req.status_code == 204)

        att = self.client.get('/api/time-attendance/1/', **add_headers())
        self.assertEqual(att.status_code, 404)
