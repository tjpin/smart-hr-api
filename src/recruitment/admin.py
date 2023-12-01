from django.contrib import admin

from .models import *

admin.site.register(Candidate)
admin.site.register(JobPosition)
admin.site.register(Interview)
admin.site.register(Application)
admin.site.register(Vacancy)
