import logging
import ntpath

from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_delete

from .models import Document


document_upload_logger = logging.getLogger('document_upload_logger')
deleted_document_logger = logging.getLogger('deleted_document_logger')


@receiver(signal=post_save, sender=Document)
def upload_document(sender, instance, created, **kwargs):
    if created:
        document_upload_logger.info("[{}] : [{}] uploaded for [{}].".format(
            instance.document_id, ntpath.basename(instance.file.name), instance.staff.full_name))
    else:
        document_upload_logger.info("[{}] : [{}] updated for [{}].".format(
            instance.document_id, ntpath.basename(instance.file.name), instance.staff.full_name))


@receiver(signal=post_delete, sender=Document)
def docs_delete(sender, instance, **kwargs):
    deleted_document_logger.warning("[{}] : [{}] Deleted for [{}].".format(
        instance.document_id, ntpath.basename(instance.file.name), instance.staff.full_name))
