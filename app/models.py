from django.db import models

# Create your models here.

class candidates(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=200)
class interview(models.Model):
    iid=models.AutoField(primary_key=True)
    i_name=models.CharField(max_length=200)
    st=models.CharField(max_length=200)
    et=models.CharField(max_length=200)
    cand=models.CharField(max_length=200)
