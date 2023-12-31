from utils.constants import DEFAULT_AUTH, DEFAULT_PERMS
from src.administration.engagement import *
from src.administration.serializers import *
from api.rest import *


# Feedback
class FeedbackListCreateAPIView(StaffListRetrieveMixin):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer
    authentication_classes = DEFAULT_AUTH
    permission_classes = DEFAULT_PERMS


# Question
class QuestionListCreateAPIView(CreateListRetrieveViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = DEFAULT_AUTH
    permission_classes = DEFAULT_PERMS


# Survey
class SurveyListCreateAPIView(SurveyCreateListRetrieveViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    authentication_classes = DEFAULT_AUTH
    permission_classes = DEFAULT_PERMS


# SurveyResponse
class SurveyResponseListCreateAPIView(StaffListRetrieveMixin):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer
    authentication_classes = DEFAULT_AUTH
    permission_classes = DEFAULT_PERMS


# Attendance
class AttendanceListCreateAPIView(CreateListRetrieveViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    authentication_classes = DEFAULT_AUTH
    permission_classes = DEFAULT_PERMS


# Leaves
class LeaveRequestListCreateAPIView(CreateListRetrieveViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    authentication_classes = DEFAULT_AUTH
    permission_classes = DEFAULT_PERMS


# Trainings
class TrainingProgramListCreateAPIView(CreateListRetrieveViewSet):
    queryset = TrainingProgram.objects.all()
    serializer_class = TrainingProgramSerializer
    # authentication_classes = DEFAULT_AUTH
    # permission_classes = DEFAULT_PERMS


# class TrainingEnrollmentListCreateAPIView(CreateListRetrieveViewSet):
#     queryset = TrainingEnrollment.objects.all()
#     serializer_class = TrainingEnrollmentSerializer


# Performances
class PerformanceReviewListCreateAPIView(CreateListRetrieveViewSet):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer
    authentication_classes = DEFAULT_AUTH
    permission_classes = DEFAULT_PERMS
