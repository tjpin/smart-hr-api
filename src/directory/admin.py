import ntpath
from django.contrib import admin

from .models import *


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ["document_id", "owner", "date_uploaded", "public_document", "archived"]
    list_display_links = ("document_id", "owner")
    list_filter = ("is_public", "archived")
    readonly_fields = ("document_id",)

    def public_document(self, obj):
        if obj.is_public:
            return True
        return False

    def owner(self, obj):
        return obj.staff


@admin.register(Transmital)
class TransmitalAdmin(admin.ModelAdmin):
    list_display = (
        "transmital_id",
        "date_submitted",
        "expected_return_date",
        "date_returned",
        "transmital_return_status",
        "purpose",
        "submitted_by",
        "referred_to",
        "approved_by",
        "status",
    )
    readonly_fields = ("transmital_id",)
    list_filter = ("status", "purpose")


@admin.register(FormDocument)
class FormDocumentAdmin(admin.ModelAdmin):
    list_display = ("form_id", "date_uploaded", "form_name", "form_type", "uploaded_by")
    list_filter = ("form_id", "date_uploaded", "form_type", "uploaded_by")
    search_fields = ("form_id", "date_uploaded", "form_type", "uploaded_by")
    readonly_fields = ("form_id",)

    def form_name(self, obj):
        return ntpath.basename(obj.form.path)


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    list_display = ("document_name", "date_archived")

    def document_name(self, obj):
        return ntpath.basename(obj.document.file.path)
