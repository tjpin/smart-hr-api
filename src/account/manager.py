from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class StaffUserManager(BaseUserManager):

    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError(_("Phone number is required."))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields['is_staff'] == False:
            raise ValueError(_("is_staff must be set to True"))
        if extra_fields['is_superuser'] == False:
            raise ValueError(_("is_superuser must be set to True"))

        return self.create_user(phone_number, password, **extra_fields)
