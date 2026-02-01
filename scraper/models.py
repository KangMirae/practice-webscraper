from django.db import models

# Create your models here.
class ScrapedData(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class EcommerceProduct(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    description = models.TextField()
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title