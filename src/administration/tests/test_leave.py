from datetime import datetime as dt
import json

from django.test import TestCase
from django.utils import timezone

from src.administration.models import *
from utils.options import LeaveStatus, LeaveType
from src.account.models import Staff, StaffUser
from utils.base_test import (create_test_user, add_headers, random_staffs)


class LeaveRequestTestCase(TestCase):
    def setUp(self):
        create_test_user(StaffUser)
        _staff = Staff.objects.create(
            staff_id='1098016210675962',
            first_name='Jane',
            middle_name="Mills",
            last_name="Doe",
            date_of_birth=timezone.now().strftime('%Y-%m-%d'),
            phone_number=12345689
        ).save()
        self.staff = Staff.objects.first()
        _leave = LeaveRequest.objects.create(
            staff=self.staff,
            leave_type=LeaveType.ANNUAL,
            status=LeaveStatus.APPROVED,
            start_date=dt(2023, 7, 15).date(),
            end_date=dt(2023, 8, 15).date(),
        )
        _leave.save()

    def test_leave_created(self):
        leave = LeaveRequest.objects.first()
        self.assertTrue(leave.status == LeaveStatus.APPROVED)
        self.assertTrue(leave.leave_type == LeaveType.ANNUAL)
        self.assertEqual(leave.staff.staff_id, "1098016210675962")
        self.assertEqual(leave.staff.first_name, "Jane")

    def test_leave_post(self):
        data = {
            "staff": self.staff.pk,
            "leaveType": "Annual",
            "leaveStatus": "Approved",
            "startDate": "2023-08-20",
            "endDate": "2023-09-20",
        }
        req = self.client.post('/api/leave-requests/',
                               data=data, content_type="application/json", **add_headers())
        self.assertTrue(req.status_code == 201)

    def test_leave_get(self):
        req = self.client.get('/api/leave-requests/', **add_headers())
        self.assertEqual(req.status_code, 200)
        self.assertTrue(len(req.json()) == 1)

    def test_leave_put(self):
        # get original object
        _leave = self.client.get('/api/leave-requests/1/', **add_headers())
        leave = _leave.json()
        data = {
            "staff": leave.get("staff"),
            "leaveType": LeaveType.PATERNITY,
            "status": LeaveStatus.DONE,
            "startDate": leave.get("startDate"),
            "endDate": leave.get("endDate")
        }
        # update
        req = self.client.put('/api/leave-requests/1/',
                              data=data, content_type="application/json", **add_headers())
        # get updated
        _req = self.client.get('/api/leave-requests/1/', **add_headers())
        _updated = _req.json()
        # test original request
        self.assertTrue(req.status_code == 200)
        # test updates object
        self.assertTrue(_updated.get('status') == LeaveStatus.DONE)
        self.assertTrue(_updated.get('leaveType') == LeaveType.PATERNITY)

    def test_leave_delete(self):
        req = self.client.delete('/api/leave-requests/1/', **add_headers())
        self.assertTrue(req.status_code == 204)
        _leave = self.client.get('/api/leave-requests/1/', **add_headers())
        self.assertTrue(_leave.status_code == 404)
