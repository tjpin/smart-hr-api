from django.contrib import admin

from .models import *
from .bank import Bank


@admin.register(PayrollRecord)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ['staff', 'net_pay']

    def net_pay(self, obj):
        return obj.net_pay


admin.site.register(Bank)
admin.site.register(TaxInformation)
admin.site.register(Benefit)
admin.site.register(Allowance)
admin.site.register(Deduction)
admin.site.register(SalaryStructure)
admin.site.register(SalaryComponent)
