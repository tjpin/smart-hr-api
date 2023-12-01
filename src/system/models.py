from django.db import models

from src.account.staff import Staff


class SystemSettings(models.Model):
    organization = models.CharField(max_length=100)
    mobile_number = models.IntegerField(null=True, blank=True)
    tel_number = models.IntegerField(null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    tag_line = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(
        upload_to='media/system/logo', null=True, blank=True)
    working_hours = models.TextField(max_length=255, null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    capital = models.DecimalField(
        max_digits=16, decimal_places=2, null=True, blank=True)
    date_established = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.organization

    class Meta:
        verbose_name = "SystemSetting"
        verbose_name_plural = "SystemSettings"

    @property
    def company_size(self):
        return str(Staff.objects.count())
