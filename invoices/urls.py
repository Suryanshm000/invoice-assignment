from django.urls import path
from . import views

app_name = 'invoices'

urlpatterns = [
    path('invoices/', views.InvoiceListAPIView.as_view(), name='invoice-list'),
    path('invoice/create/', views.InvoiceCreateAPIView.as_view(), name='invoice-create'),
    path('invoices/<int:pk>/', views.InvoiceRetrieveUpdateDestroyAPIView.as_view(), name='invoice-retrieve-update-destroy'),
    path('invoice-detail/create/', views.InvoiceDetailListCreateAPIView.as_view(), name='invoice-detail-create'),
    path('invoice-details/', views.InvoiceDetailListCreateAPIView.as_view(), name='invoice-detail-list'),
    path('invoice-details/<int:pk>/', views.InvoiceDetailRetrieveUpdateDestroyAPIView.as_view(), name='invoice-detail-retrieve-update-destroy'),
]