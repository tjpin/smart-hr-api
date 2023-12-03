from rest_framework import serializers

from .engagement import *
from src.administration.models import (
    LeaveRequest,
    PerformanceReview,
    Attendance,
)
from src.administration.development import TrainingProgram, TrainingFile, TrainingMaterial, TrainingVideo


class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class SurveyResponseSerializer(serializers.ModelSerializer):
    # survey = SurveySerializer(read_only=True)

    class Meta:
        model = SurveyResponse
        fields = "__all__"


class SurveySerializer(serializers.ModelSerializer):
    survey_responses = serializers.SerializerMethodField()

    class Meta:
        model = Survey
        fields = "__all__"

    def get_survey_responses(self, obj):
        data = SurveyResponseSerializer(obj.list_survey_responses, many=True).data
        return data


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"

    def get_hours_worked(self, obj):
        return obj.hours_worked


class LeaveRequestSerializer(serializers.ModelSerializer):
    # staff = StaffSerializer(read_only=True, required=False)

    class Meta:
        model = LeaveRequest
        fields = "__all__"


class StaffTrainingSerializer(serializers.ModelSerializer):
    program = serializers.CharField(source="program_name")
    description = serializers.CharField(source="program_description")

    class Meta:
        model = TrainingProgram
        fields = ["program", "description", "start_date", "end_date"]


class PerformanceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReview
        fields = "__all__"


class TrainingProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingProgram
        fields = "__all__"


class TrainingFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingFile
        fields = "__all__"


class TrainingMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingMaterial
        fields = "__all__"
    

class TrainingVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingVideo
        fields = "__all__"
    
