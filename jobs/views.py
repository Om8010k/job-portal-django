from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404

from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer
from .permissions import IsEmployer, IsCandidate


# ================= JOB LIST + CREATE =================
class JobCreateListView(generics.ListCreateAPIView):
    """
    GET → list all jobs
    POST → create job (only employer)
    """

    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsEmployer()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)


# ================= JOB DETAIL =================
class JobDetailView(generics.RetrieveAPIView):
    """
    Get single job details
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer


# ================= APPLY JOB =================
class ApplicationCreateView(generics.CreateAPIView):
    """
    Candidate applies to a job
    """

    serializer_class = ApplicationSerializer
    permission_classes = [IsCandidate]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['job'] = get_object_or_404(Job, id=self.kwargs['job_id'])
        return context

    def perform_create(self, serializer):
        job = get_object_or_404(Job, id=self.kwargs['job_id'])

        serializer.save(
            applicant=self.request.user,
            job=job
        )


# ================= MY APPLICATIONS =================
class MyApplicationsView(generics.ListAPIView):
    """
    Get logged-in user's applications
    """

    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(
            applicant=self.request.user
        ).order_by('-id')


# ================= JOB APPLICANTS =================
class ApplicantsView(generics.ListAPIView):
    """
    Get all applicants for a job (only employer)
    """

    serializer_class = ApplicationSerializer
    permission_classes = [IsEmployer]

    def get_queryset(self):
        job = get_object_or_404(Job, id=self.kwargs['job_id'])

        # 🔒 Only job owner can see applicants
        if job.posted_by != self.request.user:
            return Application.objects.none()

        return Application.objects.filter(job=job).order_by('-id')


# ================= FRONTEND VIEWS =================
def home(request):
    return render(request, 'index.html')


def auth_page(request):
    return render(request, 'auth.html')


def job_list(request):
    return render(request, 'jobs.html')


def job_detail(request, id):
    return render(request, 'job_detail.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def applications_page(request):
    return render(request, 'applications.html')