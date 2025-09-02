from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.username} - {self.amount} - {self.category.name}'

