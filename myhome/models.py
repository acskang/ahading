from django.db import models

# Create your models here.
class WEB_DOCUMENT(models.Model):
  id = models.IntegerField(primary_key=True)
  category = models.CharField(max_length=10)
  title = models.CharField(max_length=100)
  content = models.TextField()