from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models import Sum

from .models import PayrollRecord


@receiver(signal=post_save, sender=PayrollRecord)
def set_net_pay(sender, instance, created, **kwargs):
    # if created:
    allowances = sum([i.amount for i in instance.allowances.all()])
    deductions = sum([i.amount for i in instance.deductions.all()])

    if deductions is None and allowances is None:
        return
    if allowances:
        _allowances = float(allowances)
    if deductions:
        _deductions = float(deductions)

    instance.net_pay = (instance.basic_pay + instance.bonus +
                        allowances) - deductions
    if created:
        instance.save()

