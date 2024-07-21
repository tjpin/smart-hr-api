import base64
from datetime import datetime as dt


''' This are reusable methods '''


def create_test_user(StaffUser):
    contacts = [12345678900, 3265478966, 4785326513]
    
    for num in contacts:
        _user = StaffUser.objects.create(
            is_active=True,
            is_staff=True,
            is_superuser=True,
            phone_number=num
        )
        _user.set_password('user'+str(num))
        _user.save()


def add_headers() -> dict:
    _creds = "12345678900:admin.123"
    return {
        'HTTP_AUTHORIZATION': f'Basic {base64.b64encode(_creds.encode()).decode()}'}


def create_staff(Staff):
    _staff = Staff(
        staff_id=5460579761,
        first_name='Mike',
        middle_name="K",
        last_name="Jude",
        phone_number=12365975,
        joining_date="2023-04-20",
        date_of_birth="1997-08-14"
    )
    _staff.save()


def random_staffs(Staff, Department):
    deparment = Department.objects.create(
        department_name="Administration").save()
    deparment1 = Department.objects.create(
        department_name="Accounts").save()
    deparment2 = Department.objects.create(
        department_name="Hr Department").save()

    dpt1 = Department.objects.get(department_name="Administration")

    for i in range(10):
        Staff(
            staff_id=i,
            first_name="Test",
            middle_name=f"User {i}",
            last_name=f"Staff {i}",
            department=dpt1,
            phone_number=12345678 + i,
            date_of_birth=dt.now()
        ).save()
