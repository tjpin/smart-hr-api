from rest_framework import serializers
from src.finance.bank import Bank

from src.finance.models import *


class SalaryStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryStructure
        fields = "__all__"


class SalaryComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryComponent
        fields = "__all__"


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class DeductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deduction
        fields = "__all__"


class AllowanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allowance
        fields = "__all__"


class PayrollRecordSerializer(serializers.ModelSerializer):
    net_pay = serializers.SerializerMethodField()
    deductions = DeductionSerializer(many=True, read_only=True)
    allowances = AllowanceSerializer(many=True, read_only=True)

    class Meta:
        model = PayrollRecord
        fields = "__all__"

    def get_net_pay(self, obj):
        return obj.net_pay


class TaxInformationSerializer(serializers.ModelSerializer):
    # staff = StaffSerializer(read_only=True)

    class Meta:
        model = TaxInformation
        fields = "__all__"


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = "__all__"
