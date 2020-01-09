from django.db import models

# Create your models here.
class Place(models.Model):
    place_name=models.CharField(max_length=255)
    place_phone=models.IntegerField()
    place_address=models.CharField(max_length=255)
    rating=models.PositiveIntegerField()
    #place_img=models.ImageField()

    def __str__(self):
        return 'Name {} # {} {} Rating: {}'.format(self.place_name, self.place_phone, self.place_address, self.place_address)
