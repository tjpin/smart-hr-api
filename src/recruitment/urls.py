from rest_framework.routers import DefaultRouter

from .api_view import *

router = DefaultRouter()

router.register(r"candidates", CandidateViewSet, basename="candidates")
router.register(r"job-positions", JobPositionViewSet, basename="job-positions")
router.register(r"interviews", InterviewViewSet, basename="interviews")
router.register(r"applications", ApplicationViewSet, basename="applications")
router.register(r"vacancies", VacancyViewSet, basename="vacancies")

urlpatterns = router.urls
