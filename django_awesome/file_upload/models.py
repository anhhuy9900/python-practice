from django.db import models

# Create your models here.


class Profile(models.Model):
    image = models.FileField(upload_to="images")

    def __str__(self):
        return f"image={self.image}"