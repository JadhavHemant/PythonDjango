from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    persentage=models.FloatField()
    class Meta:
        db_table="tblstudents"