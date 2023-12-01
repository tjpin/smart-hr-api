from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models


def validate_end_date(value):
    if value <= 1:
        raise ValidationError(_("End date cannot be equal or less than start date"))


class TitleCaseField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(TitleCaseField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if isinstance(value, str):
            return self.to_python(value.title())
        return self.to_python(value)
