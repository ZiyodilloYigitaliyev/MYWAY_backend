from django.urls import path
from .views import AffidavitView, RestoreLicenseView, DepartmentView
urlpatterns = [
    # Affidavit URLs
    path('affidavits/', AffidavitView.as_view(), name='affidavits'),
    # RestoreLicense URLs
    path('restore-licenses/', RestoreLicenseView.as_view(), name='restore_licenses'),
    # Department URLs
    path('departments/', DepartmentView.as_view(), name='departments'),
]

