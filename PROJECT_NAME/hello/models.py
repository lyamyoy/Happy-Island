from django.db import models

# Create your models here.
class Model(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	author = models.CharField(max_length=50)
	image = models.ImageField(upload_to='')
	good = models.IntegerField(null=True, blank=True, default=0)