
from django.utils.translation import gettext_lazy as _
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import views as auth_views
from django.contrib.auth.tokens import default_token_generator

# my models
from .mixins import (CreateListRetrieveViewSet, StaffListRetrieveMixin,
                     SurveyCreateListRetrieveViewSet)
from src.administration.models import (
    LeaveRequest, PerformanceReview, Attendance)
from src.finance.models import (
    Benefit, PayrollRecord, SalaryComponent, SalaryStructure, TaxInformation)
from src.account.models import StaffUser
from src.account.staff import EmployeeGrade, Staff, Department
from utils.options import *
