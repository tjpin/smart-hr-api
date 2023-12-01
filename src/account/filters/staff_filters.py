from rest_framework_filters import filters, FilterSet


from src.account.staff import Staff, Department, EmployeeGrade, WorkPlace
from utils.filter_defaults import DEFAULT_FIELDS


class EmployeeGradeFilter(FilterSet):
    class Meta:
        model = EmployeeGrade
        fields = {
            "department_name": DEFAULT_FIELDS,
        }


class DepartmentFilter(FilterSet):
    class Meta:
        model = Department
        fields = {
            "department_name": DEFAULT_FIELDS,
        }


class WorkplaceFilter(FilterSet):
    class Meta:
        model = WorkPlace
        fields = {
            "work_place": DEFAULT_FIELDS,
        }


class StaffFilter(FilterSet):
    department = filters.RelatedFilter(
        DepartmentFilter, field_name="department", queryset=Department.objects.all()
    )
    grade = filters.RelatedFilter(
        EmployeeGradeFilter, field_name="grade", queryset=EmployeeGrade.objects.all()
    )
    work_place = filters.RelatedFilter(
        WorkplaceFilter, field_name="work_place", queryset=WorkPlace.objects.all()
    )

    class Meta:
        model = Staff
        fields = {
            "staff_id": DEFAULT_FIELDS,
            "first_name": DEFAULT_FIELDS,
            "middle_name": DEFAULT_FIELDS,
            "last_name": DEFAULT_FIELDS,
            "email": DEFAULT_FIELDS,
            "phone_number": DEFAULT_FIELDS,
            "grade": DEFAULT_FIELDS,
            "department": DEFAULT_FIELDS,
            "work_place": DEFAULT_FIELDS,
        }
