import logging

from django.dispatch import receiver
from django.db.models.signals import pre_save

from .models import SystemSettings
settings_logger = logging.getLogger('settings_logger')

''' Settings signals '''


def create_settings(instance):
    return SystemSettings(
        organization=instance.organization,
        address=instance.address,
        capital=instance.capital,
        date_established=instance.date_established,
        industry=instance.industry,
        mobile_number=instance.mobile_number,
        tag_line=instance.tag_line,
        tel_number=instance.tel_number,
        working_hours=instance.working_hours,
        zip_code=instance.zip_code
    )


@receiver(pre_save, sender=SystemSettings)
def update_settiings(sender, instance, **kwargs):
    settings = SystemSettings.objects.all()
    if settings.exists():
        settings.delete()
        create_settings(instance)
        settings_logger.info(
            "Old settings overwriten")
    else:
        settings_logger.info("New settings created")
        create_settings(instance)
