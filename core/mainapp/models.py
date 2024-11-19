from django.db import models

class Service(models.Model):
    # Sid is an auto-incrementing primary key by default
    Sid = models.AutoField(primary_key=True)
    Sname = models.CharField(max_length=255)
    SImage = models.ImageField(upload_to='services/images/')  # Adjust the path as necessary

    def __str__(self):
        return self.Sname
    
class CatServices(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    image = models.ImageField(upload_to='services/images/')  # Adjust the path as necessary
    serviceId = models.ForeignKey(Service, on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.name
    





     
