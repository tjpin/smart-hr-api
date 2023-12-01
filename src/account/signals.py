import logging

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete
from django.contrib.auth.hashers import make_password

from .staff import Staff
from .models import StaffUser

logger = logging.getLogger(__name__)

user_create_logger = logging.getLogger("user_create_logger")
user_delete_logger = logging.getLogger("user_delete_logger")
staff_delete_logger = logging.getLogger("staff_delete_logger")


@receiver(signal=post_save, sender=Staff)
def create_user_for_staff(sender, instance, created, **kwargs):
    if created:
        _ph = instance.phone_number
        password = "{}_{}".format(str(instance.last_name).lower(), _ph)
        user = StaffUser.objects.create(
            staff=instance,
            phone_number=instance.phone_number,
            is_active=True,
            is_staff=True,
            is_superuser=False,
            first_name=instance.first_name,
            last_name=instance.last_name,
            password=make_password(password),
        )
        s = Staff.objects.first()
        user.save()
        user_create_logger.info(
            "User: [{}] - [{}] created".format(s.staff_id, s.full_name)
        )


@receiver(signal=post_delete, sender=StaffUser)
def log_user_deleted(sender, instance, **kwargs):
    """Try block for testing purpose."""
    try:
        user_delete_logger.warning("[{}] Deleted!".format(instance.staff.full_name))
    except:
        pass


@receiver(signal=post_delete, sender=Staff)
def log_staff_deleted(sender, instance, **kwargs):
    _user = StaffUser.objects.filter(staff__staff_id=instance.staff_id)
    if _user.exists():
        _user.delete
        staff_delete_logger.warning(
            "[{}] : [{}] Deleted!".format(instance.staff_id, instance.full_name)
        )
    return
