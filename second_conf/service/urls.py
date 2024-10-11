from django.urls import path
from .views import (
    ServiceAddresView, TexServiceOrderView, GasView, CarOilView, AffidavitView,
    TexServiceMessageView, RestoreLicenseView, DepartmentView
)

urlpatterns = [
    # ServiceAddres URLs
    path('service-addresses/', ServiceAddresView.as_view(), name='service_addresses'),

    # TexServiceOrder URLs
    path('tex-service-orders/', TexServiceOrderView.as_view(), name='tex_service_orders'),

    # Gas URLs
    path('gas/', GasView.as_view(), name='gas'),

    # CarOil URLs
    path('car-oils/', CarOilView.as_view(), name='car_oils'),

    # Affidavit URLs
    path('affidavits/', AffidavitView.as_view(), name='affidavits'),

    # TexServiceMessage URLs
    path('tex-service-messages/', TexServiceMessageView.as_view(), name='tex_service_messages'),

    # RestoreLicense URLs
    path('restore-licenses/', RestoreLicenseView.as_view(), name='restore_licenses'),

    # Department URLs
    path('departments/', DepartmentView.as_view(), name='departments'),
]
