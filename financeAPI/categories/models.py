from django.db import models

class Category(models.Model):
    CATEGORY_TYPE = (
            ('income', 'Доход'),
            ('expense', 'Расход'),
        )
    name = models.CharField(max_length=124)
    type = models.CharField(max_length=10, choices=CATEGORY_TYPE)

    def __str__(self):
        return f'{self.name} ({self.type})'


