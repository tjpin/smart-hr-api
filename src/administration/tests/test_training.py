from datetime import datetime as dt
import json

from django.test import TestCase

from src.administration.models import *
from src.account.models import Staff, StaffUser
from utils.base_test import (create_test_user, add_headers, random_staffs)


class TrainingTestCase(TestCase):

    def setUp(self):
        create_test_user(StaffUser)
        for i in range(9):
            Staff(
                staff_id=str(i),
                first_name=f"Test",
                middle_name="Name",
                last_name=f"Staff {i}",
                phone_number=1234567 + i,
                date_of_birth=dt(int(f"199{i}"), i+1, i+2),
            ).save()
        self.staffs = Staff.objects.all()

        training = TrainingProgram.objects.create(
            program_name="HSE Training",
            program_description="Health and safety training",
            start_date=dt(2023, 7, 20).date(),
            end_date=dt(2023, 7, 20).date(),
        )
        training.staffs.set(self.staffs)
        training.save()

        self.trainings = TrainingProgram.objects.all()
        self.training = TrainingProgram.objects.first()

    def test_training_crested(self):
        self.assertTrue(self.trainings.count() == 1)
        self.assertTrue(self.training.staffs.count() == 9)
        self.assertTrue(self.training.staffs.count() == self.staffs.count())

    def test_training_post(self):
        data = {
            "programName": "HSE Training",
            "programDescription": "Health and safety",
            "startDate": "2023-07-20",
            "endDate": "2023-08-10",
            "staffs": [1, 2, 3, 4]
        }
        req = self.client.post('/api/training-programs/',
                               data=data, content_type='application/json', **add_headers())
        self.assertTrue(req.status_code == 201)

    def test_training_put(self):
        req = self.client.get('/api/training-programs/1/', **add_headers())
        _trainings = req.json()
        data = {
            "programName": "IT Training",
            "programDescription": "IT and safety",
            "startDate": _trainings.get('startDate'),
            "endDate": _trainings.get('endDate'),
            "staffs": [1, 2]
        }
        _req = self.client.put('/api/training-programs/1/',
                               data=data, content_type='application/json', **add_headers())
        self.assertEqual(_req.status_code, 200)

    def test_training_delete(self):
        self.client.delete('/api/training-programs/1/', **add_headers())
        req = self.client.get('/api/training-programs/1/', **add_headers())
        self.assertTrue(req.status_code == 404)
