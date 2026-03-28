# 🚀 Job Portal (Django + DRF)

A full-stack Job Portal built using Django REST Framework with JWT Authentication and Role-Based Access Control.

---

## 🔐 Features

- User Registration & Login (JWT Authentication)
- Role-Based Access:
  - 👨‍💼 Employer → Post Jobs
  - 👨‍🎓 Candidate → Apply for Jobs
- Job Listing & Detail View
- Apply with Resume Upload 📄
- Prevent Duplicate Applications
- View Applied Jobs
- Employer can view applicants

---

## 🛠️ Tech Stack

- Backend: Django, Django REST Framework
- Authentication: JWT (SimpleJWT)
- Database: PostgreSQL
- Frontend: HTML, Tailwind CSS
- API Testing: Postman

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/job-portal-django.git
cd job-portal-django
pip install -r requirements.txt
python manage.py runserver



## 🔑 API Endpoints

| Endpoint                   | Method | Description                |
|--------------------------|--------|----------------------------|
| /api/accounts/register/   | POST   | Register new user          |
| /api/accounts/login/      | POST   | Login user                 |
| /api/jobs/                | GET    | Get all jobs               |
| /api/jobs/                | POST   | Create job (Employer only) |
| /api/jobs/<id>/           | GET    | Job detail                 |
| /api/jobs/<id>/apply/     | POST   | Apply for job              |
| /api/jobs/my-applications/| GET    | View applied jobs          |
| /api/jobs/<id>/applicants/| GET    | View applicants (Employer) |

> 🔐 Note: Protected endpoints require JWT authentication using Bearer Token.