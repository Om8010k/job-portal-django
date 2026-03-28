from rest_framework import serializers
from .models import Job, Application


class JobSerializer(serializers.ModelSerializer):
    """
    Serializer for Job model
    """

    posted_by = serializers.CharField(source='posted_by.username', read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['posted_by', 'created_at']

    def validate_salary(self, value):
        """Ensure salary is positive"""
        if value < 0:
            raise serializers.ValidationError("Salary must be positive")
        return value


class ApplicationSerializer(serializers.ModelSerializer):
    """
    Serializer for Application model
    """

    job_title = serializers.CharField(source='job.title', read_only=True)
    company_name = serializers.CharField(source='job.company_name', read_only=True)

    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['applicant', 'status', 'applied_at']

    def validate(self, data):
        """Prevent duplicate applications"""
        request = self.context.get('request')
        user = request.user if request else None
        job = data.get('job')

        if user and job:
            if Application.objects.filter(applicant=user, job=job).exists():
                raise serializers.ValidationError("You have already applied for this job.")

        return data