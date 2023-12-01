from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext as _

from utils.helpers import timestamp_id
from utils.options import DocumentType, GeneralStatus, TransmitalReasons, FormType
from src.account.staff import Staff


class FormDocument(models.Model):
    """
    This model is form specific.
    """

    form_id = models.CharField(
        verbose_name=_("Form ID"),
        max_length=10,
        primary_key=True,
        default=timestamp_id(10),
    )
    form = models.FileField(upload_to="files/office/forms/")
    date_uploaded = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    form_type = models.CharField(
        max_length=30,
        choices=FormType.choices,
        default=FormType.GENERAL_FORM,
    )
    is_public = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Form Document"
        verbose_name_plural = "Form Documents"
        ordering = ("-date_uploaded",)

    def __str__(self) -> str:
        return self.form.name


class Document(models.Model):
    document_id = models.CharField(max_length=16, default=timestamp_id(10))
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    document_type = models.CharField(
        max_length=100, default=DocumentType.DEFAULT, choices=DocumentType.choices
    )
    file = models.FileField(upload_to="files/user/files/")
    date_uploaded = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=20, default=GeneralStatus.DEFAULT, choices=GeneralStatus.choices
    )
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.staff.full_name

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"


class Transmital(models.Model):
    transmital_id = models.CharField(
        max_length=16, default=timestamp_id(12), primary_key=True
    )
    transmital = models.FileField(upload_to="files/office/transmitals/")
    referred_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="receiving_user",
    )
    submitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="submiting_user",
    )
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="approving_user",
    )
    purpose = models.CharField(
        max_length=50,
        choices=TransmitalReasons.choices,
        default=TransmitalReasons.DEFAULT,
    )
    date_submitted = models.DateField(default=timezone.now)
    expected_return_date = models.DateField(default=timezone.now)
    date_returned = models.DateField(default=timezone.now)
    status = models.CharField(
        max_length=50, choices=GeneralStatus.choices, default=GeneralStatus.DEFAULT
    )

    def __str__(self):
        return str(self.transmital_id)

    @property
    def transmital_return_status(self) -> str:
        """
        - Track remaining days from date submited to expected return date.
        - Returns a string with date diffrence in days (int).
        """
        diff = self.expected_return_date - timezone.now().date()
        if diff.days == 0:
            return "Due for return today"
        elif diff.days == 1:
            return "Late with 1 day"
        elif diff.days == -1:
            return "Due in 1 day"
        elif diff.days > 1:
            return "{} days remaining to return this document".format(abs(diff.days))
        else:
            return "Late with {} days".format(abs(diff.days))

    class Meta:
        ordering = ["-date_submitted"]
        verbose_name = "Transmital"
        verbose_name_plural = "Transmitals"


class Archive(models.Model):
    """Store archived files."""

    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    date_archived = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.document.file.name

    class Meta:
        ordering = ["-date_archived"]
        verbose_name = "Archive"
        verbose_name_plural = "Archives"
