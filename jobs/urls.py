from django.urls import path
from .views import (
    JobCreateListView,
    ApplicationCreateView,
    JobDetailView,
    MyApplicationsView,
    ApplicantsView
)

urlpatterns = [
    # JOB
    path('', JobCreateListView.as_view()),
    path('<int:pk>/', JobDetailView.as_view()),

    # APPLICATION
    path('<int:job_id>/apply/', ApplicationCreateView.as_view()),
    path('my-applications/', MyApplicationsView.as_view()),
    path('<int:job_id>/applicants/', ApplicantsView.as_view()),
]