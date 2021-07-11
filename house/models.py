from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    description = models.TextField()
    property_type = models.CharField(max_length=300)
    rent     = models.CharField(max_length=200)
    baths =   models.FloatField(default=0)
    beds = models.FloatField(default=0) 
    garage = models.FloatField(default=0) 
    date_added =  models.DateTimeField(auto_now_add = True)
    location = models.CharField(max_length=2000, default= 'lagos')
    landing_page_view = models.ImageField(upload_to = 'land/', null=True, blank = True)
    search_img = models.ImageField(upload_to = 'land/', null=True, blank = True)
    image_1 = models.ImageField(upload_to = 'picture/', null=True, blank = True)
    image_2 = models.ImageField(upload_to = 'picture/', null=True, blank = True)
    image_3 = models.ImageField(upload_to = 'picture/', null=True, blank = True)
    video   = models.FileField(upload_to='video/', null=True, blank=True)
    floor_plan = models.ImageField(upload_to='floorplan/', null=True, blank=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class Amenities(models.Model):
    house = models.ForeignKey(House, on_delete= models.CASCADE) 
    amenity = models.CharField(max_length=300)
    def __str__(self):
        return f'amenities of {self.house.name}'


