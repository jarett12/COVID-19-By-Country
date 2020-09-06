from django.db import models

class COVID(models.Model):
    globalStats= models.TextField()
    countries = models.TextField()

    def __str__(self):
        return self.globalStats