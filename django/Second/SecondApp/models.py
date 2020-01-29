from django.db import models

# Create your models here.
class Curriculum(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id) + '번 / ' + self.name
