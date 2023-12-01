from django.db import models


class  Bank(models.Model):
    bank_name = models.CharField(max_length=34)
    iban_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    telephone_number = models.IntegerField(null=True, blank=True)
    mobile_number = models.IntegerField(null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    online_portal = models.URLField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Bank"
        verbose_name_plural = "Banks"

    def __str__(self):
        return self.bank_name
