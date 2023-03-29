from django.db import models
from Uapp.models import User

# Create your models here.
class LSadmin(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    # category = models.ForeignKey(on_delete=models.CASCADE)
    estimated_time = models.IntegerField()
    start_date = models.DateField()
    completion_date = models.DateField()
    
class Meta:
    db_table ='LSadmin'