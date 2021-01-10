from django.db import models
from django.db.models.fields import DateTimeField
from datetime import datetime
# interaction with database in this case postgresql

# duh i spelt photo phtot and upload to media folder as /&Y and not /%Y
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    phtot = models.ImageField(upload_to='photos/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
        # without this def: new realtor created in dj admin and will say realtor object1 or something stupid like that


        


