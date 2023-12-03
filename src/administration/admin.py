from django.contrib import admin

from .models import *
from .engagement import *
from .development import *


admin.site.register(TrainingMaterial)
admin.site.register(TrainingProgram)
admin.site.register(TrainingVideo)
admin.site.register(TrainingFile)

admin.site.register(LeaveRequest)
admin.site.register(Attendance)
admin.site.register(PerformanceReview)


admin.site.register(Question)
admin.site.register(Survey)
admin.site.register(FeedBack)
admin.site.register(SurveyResponse)
