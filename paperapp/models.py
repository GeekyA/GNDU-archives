from django.db import models
import datetime
# Create your models here.


class Paper(models.Model):
	title = models.CharField(max_length=200,null=False,unique=True)
	pdf = models.FileField(upload_to='papers/pdfs',max_length=500)
