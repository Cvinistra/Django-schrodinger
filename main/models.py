from django.db import models
class Quote(models.Model):
    text=models.TextField()
    source=models.CharField(max_length=120,blank=True)
    order=models.PositiveIntegerField(default=0)
    class Meta:
        ordering=["order","id"]
    def __str__(self): return self.text[:60]
class GalleryItem(models.Model):
    title=models.CharField(max_length=120)
    image_url=models.URLField()
    caption=models.CharField(max_length=240,blank=True)
    order=models.PositiveIntegerField(default=0)
    class Meta:
        ordering=["order","id"]
    def __str__(self): return self.title
