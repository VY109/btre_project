from django.db import models
from datetime import datetime

class Contact(models.Model):
  listing = models.CharField(max_length=200)
  listing_id = models.IntegerField()
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)
  def __str__(self):
    return self.name

"""
1. project settings.py
      INSTALLED_APPS = [
          'contacts.apps.ContactsConfig',
2. (venv) cmd -- make migration file to sql create table
      > python manage.py makemigrations contacts
  - execute the file [contacts\migrations\0001_initial.py]
      > python manage.py migrate       
"""
