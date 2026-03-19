from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    About, Home, Contact,
    main_login, admin_login, staff_login, doctor_login, patient_login,
    Logout_admin, Index, staff_dashboard,
    staff_view_doctors, staff_view_patients, staff_billing, mark_bill_paid,
    View_Doctor, Delete_Doctor, Add_Doctor,
    View_Patient, Delete_Patient, Add_Patient,
    View_Appointment, Add_Appointment, Delete_Appointment,
    signup, admin_signup, staff_signup, doctor_signup, patient_signup,
    patient_dashboard, doctor_dashboard, doctor_appointments, doctor_prescriptions, doctor_my_patients,
    patient_book_appointment, patient_appointments, cancel_appointment, prescribe_medicine,
)

urlpatterns = [
    # Root shows login page
    path('', main_login, name='root'),

    path('about/', About, name='about'),
    path('home/', Home, name='home'),
    path('contact/', Contact, name='contact'),

    # Login & Signup
    path('login/', main_login, name='main_login'),
    path('admin-login/', admin_login, name='admin_login'),
    path('staff-login/', staff_login, name='staff_login'),
    path('doctor-login/', doctor_login, name='doctor_login'),
    path('patient-login/', patient_login, name='patient_login'),
    path('signup/', signup, name='signup'),
    path('admin-signup/', admin_signup, name='admin_signup'),
    path('staff-signup/', staff_signup, name='staff_signup'),
    path('doctor-signup/', doctor_signup, name='doctor_signup'),
    path('patient-signup/', patient_signup, name='patient_signup'),

    path('logout/', Logout_admin, name='logout_admin'),

    # Dashboards
    path('index/', Index, name='dashboard'),
    path('staff-dashboard/', staff_dashboard, name='staff_dashboard'),
    path('patient-dashboard/', patient_dashboard, name='patient_dashboard'),

    # Staff portal (new)
    path('staff/doctors/', staff_view_doctors, name='staff_view_doctors'),
    path('staff/patients/', staff_view_patients, name='staff_view_patients'),
    path('staff/billing/', staff_billing, name='staff_billing'),
    path('staff/bill/<int:bill_id>/pay/', mark_bill_paid, name='mark_bill_paid'),

    # Admin CRUD
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('view_patient/', View_Patient, name='view_patient'),
    path('view_appointment/', View_Appointment, name='view_appointment'),

    path('add_doctor/', Add_Doctor, name='add_doctor'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('add_appointment/', Add_Appointment, name='add_appointment'),

    path('delete_doctor/<int:pid>/', Delete_Doctor, name='delete_doctor'),
    path('delete_patient/<int:pid>/', Delete_Patient, name='delete_patient'),
    path('delete_appointment/<int:pid>/', Delete_Appointment, name='delete_appointment'),

    path('doctor-dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('doctor-appointments/', doctor_appointments, name='doctor_appointments'),
    path('doctor-my-patients/', doctor_my_patients, name='doctor_my_patients'),
    path('doctor-prescriptions/', doctor_prescriptions, name='doctor_prescriptions'),

    path('patient-book-appointment/', patient_book_appointment, name='patient_book_appointment'),

    path('patient-appointments/', patient_appointments, name='patient_appointments'),
    path('cancel-appointment/<int:apt_id>/', cancel_appointment, name='cancel_appointment'),
    path('doctor/prescribe/<int:patient_id>/', prescribe_medicine, name='prescribe_medicine'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)