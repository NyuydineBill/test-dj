from django.db import models

# Create your models here.

class Emissions(models.Model):
    id = models.AutoField(primary_key=True)
    Date_Created = models.DateField(auto_now=True, null=False)
    Accounting_Period = models.CharField(max_length = 150 , null=False)
    Scope_1 = models.IntegerField(null=True)
    Scope_2 = models.IntegerField(null=True)
    Scope_3 = models.IntegerField(null=True)
    
