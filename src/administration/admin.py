from django.contrib import admin

from .models import *
from .engagement import *


admin.site.register(TrainingProgram)
admin.site.register(LeaveRequest)
admin.site.register(Attendance)
admin.site.register(PerformanceReview)


admin.site.register(Question)
admin.site.register(Survey)
admin.site.register(FeedBack)
admin.site.register(SurveyResponse)
