# models.py

from django.db import models

class UploadedImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')  # will be stored in S3
    uploaded_at = models.DateTimeField(auto_now_add=True)
