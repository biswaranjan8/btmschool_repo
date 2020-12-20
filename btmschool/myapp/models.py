from django.db import models


class imagefiled(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)


class newspage(models.Model):
    image = models.ImageField(upload_to='news')
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=800)
    publish_date = models.DateTimeField()

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
