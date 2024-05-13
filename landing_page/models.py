from django.db import models


#  here we need to create the actual pages

# there is a image, a link, a description, a title and an option

class TileModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    url_link = models.URLField(max_length=200, null=True)
    pass


