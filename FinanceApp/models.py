from django.db import models
import uuid 
# Create your models here.
class  Transaction (models.Model):
    options = (
        ('$','$'),
        ('C$','C$')
        )
    
    types = (
        ('Income','Income'),
        ('Expense','Expense'),
        )
    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                                      editable=False)
    transaction_title = models.CharField(max_length=150)
    transaction_amount = models.FloatField()
    transaction_currency = models.CharField(max_length=10, choices=options)
    transaction_type = models.CharField(max_length=10, choices=types)
    transaction_creation_date = models.DateTimeField(auto_now_add=True)
    # transaction_update_date = models.DateTimeField(auto_now_add=True, on_date)
    transaction_description = models.TextField(null=True)
    transaction_keywords = models.TextField()

    def __str__(self):
        return self.transaction_title