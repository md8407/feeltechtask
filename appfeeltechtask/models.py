from msilib.schema import CheckBox
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
SUBJECT_CHOICES = {
    ("1","MATHS"),
    ("2","PHYSICS"),
    ("3","CHEMISTRY"),
}
class User(AbstractUser):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    

    class Meta():
        db_table = 'usr'

    def __str__(self):
        return self.first_name


class Inquiry(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50) 
    email = models.EmailField(max_length=254) 
    contact = models.CharField(max_length=50)
    subject = models.CharField(max_length=50,choices=SUBJECT_CHOICES, default = '1')

    class Meta():
        db_table = 'inq'
    
    def __str__(self):
        return self.first_name
    
     