from django.db import models
from django.utils.translation import gettext_lazy as _

from src.hrm import *
from src.finance.bank import Bank, StaffBankAccount
from utils.options import EducationLevels
from utils.validators import TitleCaseField


class Department(models.Model):
    department_name = TitleCaseField(max_length=255)

    def __str__(self):
        return self.department_name

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")


class WorkPlace(models.Model):
    workplace_name = TitleCaseField(max_length=255)
    address         = models.TextField(null=True, blank=True)
    openning_time   = models.TimeField(null=True, blank=True)
    clossing_time   = models.TimeField(null=True, blank=True)
    open_on_weekends = models.BooleanField(default=False)

    def __str__(self):
        return self.work_place_name

    class Meta:
        verbose_name        = _("Work Location")
        verbose_name_plural = _("Work Locations")

class EmployeeGrade(models.Model):
    grade = TitleCaseField(max_length=30)
         
    def __str__(self):
        return self.grade

    class Meta:
        verbose_name        = _("Employee Grade")
        verbose_name_plural = _("Employee Grades")

class  Staff(models.Model):
    staff_id        = TitleCaseField(max_length=16, default=timestamp_id(16), unique=True, primary_key=True)
    first_name      = TitleCaseField(max_length=255)
    middle_name     = TitleCaseField(max_length=255, null=True, blank=True)
    last_name       = TitleCaseField(max_length=255)
    email           = models.EmailField(unique=True)
    phone_number    = models.BigIntegerField(unique=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="staffs/profile/")
    date_of_birth   = models.DateField()
    gender          = TitleCaseField(max_length=14, default=GenderChoices.DEFAULT, choices=GenderChoices.choices)
    id_number       = models.BigIntegerField(null=True, blank=True, unique=True)
    address         = models.TextField(null=True, blank=True)
    joining_date    =  models.DateField(default=timezone.now)
    access_card     = TitleCaseField(max_length=12, null=True, blank=True, unique=True)
    education_level = TitleCaseField(max_length=14, choices=EducationLevels.choices, default=EducationLevels.DEFAULT)
    status          = models.CharField(max_length=20, choices=StaffStatus.choices, default=StaffStatus.ACTIVE)
    skills          = models.TextField(null=True, blank=True)
    bank_account    = models.ForeignKey(StaffBankAccount, db_column=_("staff_bank_account"), on_delete=models.SET_NULL, null=True, blank=True,)
    work_place      = models.ForeignKey(WorkPlace, on_delete=models.SET_NULL, null=True, blank=True)
    grade           = models.ForeignKey(EmployeeGrade, on_delete=models.SET_NULL, null=True, blank=True)
    department      = models.ForeignKey(Department, related_name=_("staffdepartment"), on_delete=models.SET_NULL, null=True, blank=True)
    medical_card_number = TitleCaseField(max_length=12, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["phone_number"], name="staff_phone_number_idx"),
            models.Index(fields=["id_number"], name="staff_id_number_idx"),
            models.Index(fields=["staff_id"], name="staff_staff_id_idx"),
        ]
        verbose_name        = _("Staff")
        verbose_name_plural = _("Staffs")

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def staff_documents(self):
        return self.document_set.all()

    @property
    def tax(self):
        return self.taxinformation_set.all()

    @property
    def list_trainings(self):
        return self.trainingprogram_set.all()

    def __str__(self):
        return self.full_name

    @property
    def reporting_to(self):
        if not self.department:
            return
        _department = Department.objects.get(
            department_name = self.department.department_name
        )
        _hod = HeadOfDepartment.objects.filter(department=_department)
        if _hod.exists():
            return _hod.first().hod
        return None

    @property
    def staff_payroll(self):
        return self.payrollrecord_set.all()

    @property
    def attendance(self):
        return self.attendance_set.all()

    @property
    def staff_leaves(self):
        return self.leaverequest_set.all()

class HeadOfDepartment(models.Model):
    hod         = models.ForeignKey(Staff, related_name=_("hodstaff"), on_delete=models.CASCADE)
    department  = models.ForeignKey(Department, related_name=_("hoddepartment"), on_delete=models.CASCADE)

    def __str__(self):
        return self.hod.full_name

    class Meta:
        verbose_name = _("Head of Department")
        verbose_name_plural = _("Heads of Departments")
 