from rest_framework import serializers
from .models import Transaction
from categories.models import Category

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TransactionSerializers(serializers.ModelSerializer):
    category = CategorySerializers(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all, source='category', write_only=True)
    
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'amount', 'description', 'date', 'category', 'category_id']
        read_only_fields = ['user']

