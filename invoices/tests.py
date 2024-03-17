from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice


class InvoiceAPITests(APITestCase):

    def test_create_invoice(self):
        data = {
            'customer_name': 'testuser',
            'date': '2024-03-17'
        }
        response = self.client.post('http://127.0.0.1:8000/invoices/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

    def test_view_invoice(self):
        self.test_create_invoice()
        response = self.client.get('http://127.0.0.1:8000/invoices/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_delete_invoice(self):
        self.test_create_invoice()
        response = self.client.delete('http://127.0.0.1:8000/invoices/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    
    def test_update_invoice(self):
        data = {
            'customer_name': 'testuser',
            'date': '2024-03-18'
        }
        self.test_create_invoice()
        response = self.client.put('http://127.0.0.1:8000/invoices/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class InvoiceDetailAPITest(APITestCase):

    def setUp(self):
        # creating invoice directly in the database
        self.invoice1 = Invoice.objects.create(customer_name='testuser', date='2024-03-18')

    def test_create_invoiceDetail(self):
        data = {
            'invoice': self.invoice1.id,
            'description': 'this is for testing',
            'quantity': 3,
            'unit_price': 20,
            'price': 60
        }
        response = self.client.post('http://127.0.0.1:8000/invoice-details/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_view_invoiceDetail(self):
        self.test_create_invoiceDetail()
        response = self.client.get('http://127.0.0.1:8000/invoice-details/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_invoiceDetail(self):
        self.test_create_invoiceDetail()
        response = self.client.delete('http://127.0.0.1:8000/invoice-details/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_update_invoiceDetail(self):
        self.test_create_invoiceDetail()
        data = {
            'invoice': self.invoice1.id,
            'description': 'this is for testing',
            'quantity': 3,
            'unit_price': 10,
            'price': 30.0
        }
        response = self.client.put('http://127.0.0.1:8000/invoice-details/1/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)