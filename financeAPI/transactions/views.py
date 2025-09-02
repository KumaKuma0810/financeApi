from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Transaction
from .serializers import TransactionSerializers


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializers):
        serializers.save(self.request.user)



