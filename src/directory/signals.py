import logging
import ntpath
import threading

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_delete

from .models import Document, Archive


document_upload_logger = logging.getLogger('document_upload_logger')
deleted_document_logger = logging.getLogger('deleted_document_logger')
document_archive_logger = logging.getLogger('document_archive_logger')


@receiver(signal=post_save, sender=Document)
def upload_document(sender, instance, created, **kwargs):
    if created:
        document_upload_logger.info("[{}] : [{}] uploaded for [{}]".format(
            instance.document_id, ntpath.basename(instance.file.name), instance.staff.full_name))
    else:
        document_upload_logger.info("[{}] : [{}] updated for [{}]".format(
            instance.document_id, ntpath.basename(instance.file.name), instance.staff.full_name))


@receiver(signal=post_delete, sender=Document)
def docs_delete(sender, instance, **kwargs):
    deleted_document_logger.warning("[{}] : {} - deleted for [{}]".format(
        instance.document_id, ntpath.basename(instance.file.name), instance.staff.full_name))


@receiver(signal=post_save, sender=Archive)
def update_archived_document_status(sender, instance: Archive, created, **kwargs):
    if created:
        Document.objects.filter(document_id=instance.document.document_id).update(archived=True)
    document_archive_logger.info("[{}] : {} - archived for [{}]".format(
        instance.document.document_id, ntpath.basename(instance.document.file.name), instance.document.staff.full_name))

@receiver(signal=pre_delete, sender=Archive)
def unarchived_document(sender, instance: Archive, **kwargs):    
    Document.objects.filter(document_id=instance.document.document_id).update(archived=False)
    document_archive_logger.info("[{}] : {} - restored for [{}]".format(
        instance.document.document_id, ntpath.basename(instance.document.file.name), instance.document.staff.full_name.title()))
