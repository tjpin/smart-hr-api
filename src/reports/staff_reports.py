from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Q, QuerySet as Qs

from src.account.staff import (
    Staff,
    Department,
    EmployeeGrade,
    EducationLevels,
    WorkPlace,
)
from utils.options import GenderChoices, StaffStatus

__all__ = ["StaffReports"]


class StaffReports(Staff):
    """Staff model summarized report.

    Args:
        Staff (models.Model): Staff db object
    """
    def __init__(self, *args, **kwargs):
        super(StaffReports, self).__init__(*args, **kwargs)
        self.staffs = self.objects.all()
        self.departments = Department.objects.all()
        self.grades = EmployeeGrade.objects.all()
        self.workplaces = WorkPlace.objects.all()

    @property
    def __total_stafffs(self) -> int:
        return self.staffs.count()
    
    @property
    def __active_staffs(self) -> list:
        return list(self.staffs.filter(status=StaffStatus.ACTIVE).order_by("-joining_date").all())
    
    @property
    def __staffs_on_leave(self) -> list:
        return list(self.staffs.filter(status=StaffStatus.ON_LEAVE).order_by("-joining_date").all())

    @property
    def __staffs_per_department(self) -> dict:
        departments = {}
        for staff in self.staffs:
            self.__evaluate__(staff.department, departments.keys(), staff, departments)
        return departments

    @property
    def __staffs_per_grade(self) -> dict:
        grades = {}
        for staff in self.staffs:
            self.__evaluate__(staff.grade, grades.keys(), staff, grades)
        return grades

    @property
    def __graduates(self) -> dict:
        """Filter only staffs with any of [Bachelor, Degree, Masters, Doctorate]

        Returns:
            dict: Dictionary of graduate staffs.
        """
        _levels = {"Bachelor", "Degree", "Masters", "Doctorate"}
        graduates = {}
        filtered = self.staffs.filter(
            Q(education_level=EducationLevels.BACHELOR) |
            Q(education_level=EducationLevels.DEGREE) |
            Q(education_level=EducationLevels.MASTERS) |
            Q(education_level=EducationLevels.DOCTORATE)
        ).all()
        
        for staff in filtered:
            self.__evaluate__(staff.education_level, _levels, staff, graduates)
        return graduates

    @property
    def __staffs_per_workplace(self) -> dict:
        places = {}
        for staff in self.staffs:
            self.__evaluate__(staff.work_place, places.keys(), staff, places)
        return places

    @property
    def __suspended_staffs(self) -> list:
        return list(self.staffs.filter(status=StaffStatus.SUSPENDED).all())

    @property
    def __upcoming_birthdays(self) -> list:
        """Get all upcoming birthdays 3 days in advance.

        Returns:
            list: List of staffs with upcoming birthdays.
        """
        now = datetime.now().date()
        upcoming = now + timedelta(days=3)
        return list(self.objects.filter(date_of_birth__range=[now, upcoming]).all())
    
    @property
    def __staffs_by_gender(self) -> dict:
        male = self.staffs.filter(gender=GenderChoices.MALE).count()
        females = self.staffs.filter(gender=GenderChoices.FEMALE).count()
        unknown = self.staffs.filter(gender=GenderChoices.OTHER).count()
        return {
            "male": male,
            "females": females,
            "unknown": unknown
        }
    
    @classmethod
    def __evaluate__(cls, field, objects, staff: Staff, results: dict):
        """Helper method to reduce redudancy.

        Args:
            field (_type_): model field to evaluate
            objects (_type_): queryset of list of model instances.
            staff (Staff): single staff instance.
            results (dict): evaluation results
        """
        if not isinstance(objects, list) or not isinstance(objects, Qs):
            raise ValueError("objects must be a list of objects or a Queryset")
        if field in objects:
            results[field].append(staff)
        else:
            results[field] = [staff]

    def reports(self):
        """Generate staff model report.

        Returns:
            _type_: Dictionary
        """
        return {
            "total_staffs":             self.__total_stafffs,
            "staffs_per_departments":   self.__staffs_per_department,
            "staffs_per_pay_grades":    self.__staffs_per_grade,
            "staffs_per_work_places":   self.__staffs_per_workplace,
            "active_staffs":            self.__active_staffs,
            "staffs_on_leave":          self.__staffs_on_leave,
            "suspended":                self.__suspended_staffs,
            "graduates":                self.__graduates,
            "genders":                  self.__staffs_by_gender,
            "upcoming_birthdays":       self.__upcoming_birthdays,
        }
