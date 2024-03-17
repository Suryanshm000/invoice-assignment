from rest_framework import serializers
from .models import Invoice, InvoiceDetail
import datetime

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'customer_name', 'date']

    # def create(self, validated_data):
    #     # Parse date into date objects
    #     validated_data['date'] = datetime.date.today()

    #     return Invoice.objects.create(**validated_data)
    
class InvoiceViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'