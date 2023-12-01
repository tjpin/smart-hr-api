from django.contrib.auth import get_user_model
from rest_framework import viewsets

from api.rest import *
from api.mixins import CreateListRetrieveViewSet

# from src.account.filters.staff_filters import StaffFilter
from src.account.models import StaffUser
from src.account.serializers import (
    EmployeeGradeSerializer,
    UserResetPasswordSerializer,
    UserSerializer,
    StaffSerializer,
    DepartmentSerializer,
)
from src.account.staff import Department, EmployeeGrade, Staff
from utils.constants import DEFAULT_PERMS, DEFAULT_AUTH

# , DEFAULT_FILTER_BACKENDS


# Staff
class StaffListCreateAPIView(CreateListRetrieveViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    # filter_backends = DEFAULT_FILTER_BACKENDS
    # filter_class = StaffFilter
    authentication_classes = DEFAULT_AUTH
    permission_classes = DEFAULT_PERMS


# Departments
class DepartmentListCreateAPIView(CreateListRetrieveViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = DEFAULT_AUTH
    permission_classes = DEFAULT_PERMS


# EmployeeGrade
class GradeRetrieveUpdateDestroyAPIView(CreateListRetrieveViewSet):
    queryset = EmployeeGrade.objects.all()
    serializer_class = EmployeeGradeSerializer
    authentication_classes = DEFAULT_AUTH
    permission_classes = DEFAULT_PERMS


# Users
class UserListCreateAPIView(CreateListRetrieveViewSet):
    queryset = StaffUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = DEFAULT_AUTH
    permission_classes = DEFAULT_PERMS


User = get_user_model()
# Reset password


class UserResetPasswordViewset(viewsets.ModelViewSet, APIView):
    serializer_class = UserResetPasswordSerializer
    queryset = User.objects.all()
    authentication_classes = DEFAULT_AUTH
    permission_classes = DEFAULT_PERMS

    @classmethod
    def get_extra_actions(cls):
        return []

    def put(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # otp = serializer.validated_data['opt']
        email = serializer.validated_data["email"]

        search_user = User.objects.filter(staff__email=email)
        if search_user.exists():
            user = search_user.first()

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            reset_link = "{}/password-reset/{}/{}/".format(
                settings.FRONTEND_URL, uid, token
            )

            subject = "Password Reset"
            message = render_to_string(
                "password_reset_email.html",
                {
                    "reset_link": reset_link,
                },
            )
            email_message = EmailMessage(
                subject,
                message,
                to=["chairman@iname.com"],
                from_email=settings.EMAIL_HOST,
            )
            email_message.send()
            return Response({"Success": "Password reset email sent."})
        return Response({"Info": "Done"})
