from django.test import TestCase

from src.finance.models import *
from utils.base_test import *
from src.account.models import StaffUser


class SalaryComponentTestCase(TestCase):
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

        _component = SalaryComponent.objects.create(
            component_name='Test',
            component_type="New",
            percentage=15.00,
            structure=self.structure
        )

        self.component = SalaryComponent.objects.first()

    def test_component_create(self):
        self.assertTrue(self.component.pk == 1)
