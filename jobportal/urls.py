from django.contrib import admin
from django.urls import path, include
from jobs.views import home, auth_page, job_list, job_detail, dashboard
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from jobs.views import applications_page
urlpatterns = [
    path('admin/', admin.site.urls),

    # ================= FRONTEND =================
    path('', home),                         # Home Page
    path('auth/', auth_page),               # Login/Register
    path('jobs/', job_list),                # Jobs List
    path('jobs/<int:id>/', job_detail),     # Job Detail
    path('dashboard/', dashboard),          # Dashboard
    path('applications/', applications_page), # Applications Page

    # ================= API =================
    path('api/accounts/', include('accounts.urls')),
    path('api/jobs/', include('jobs.urls')),

    # ================= DOCS =================
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    
]