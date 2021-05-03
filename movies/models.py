from django.db import models

# Create your models here.


class Moviedata(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    rating = models.FloatField()
    duration = models.FloatField()
    typ = models.CharField(max_length=200, default='action')
    image = models.ImageField(default='Images/None/Noimg.png', upload_to='Images')
