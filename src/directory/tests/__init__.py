from pathlib import Path

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from src.directory.models import Document, Transmital
from utils.base_test import *
from src.account.models import Staff, StaffUser


class DocumentTestCase(TestCase):
    def setUp(self):
        create_test_user(StaffUser)
        create_staff(Staff)

        self.staff = Staff.objects.first()
        self.user = StaffUser.objects.first()

        self.path = Path(__name__).resolve().parent
        self.filepath = self.path / 'src/directory/tests'
        self.filename = self.filepath / 'cv.png'

        self.file = SimpleUploadedFile('cv.png', b"")

        _document = Document.objects.create(
            staff=self.staff,
            is_public=False,
            file=self.file
        )
        _transmital = Transmital.objects.create(
            transmital=self.file,
            approved_by=self.user,
            submitted_by=self.user,
            referred_to=self.user
        )
        _transmital.save()
        _document.save()

        self.transmital = Transmital.objects.all()
        self.document = Document.objects.filter(pk=1)

    def test_document_created(self):
        self.assertTrue(self.document.exists())
        self.assertEqual(self.document.first().staff.staff_id,
                         self.staff.staff_id)

    def test_client_view(self):
        res = self.client.get('/api/documents/', **add_headers())
        self.assertTrue(
            res.resolver_match.func.initkwargs['basename'] == 'documents')
