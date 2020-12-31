vscode complains abt && separator not workin
> git add . && git commit -m 'Initial commit'
so replaced with 
> git add . | git commit -m 'Initial commit'

?
  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

  to set your account's default identity.
Omit --global to set the identity only in this repository.

[django server] -- port 8000 is already used up so 8080
> python manage.py runserver 8080

[django project] -- start new project in current location . 
> django.admin startproject btre .

[django apps] - urls.py is not in by default 
> python manage.py startapp pages
> python manage.py startapp listings

[virtual environment]
 python -m venv ./venv -- to create virtual environment
./venv/Scripts/activate.ps1 -- if powershell terminal
venv\scripts\deactivate.bat and activate.bat

[syntax]
{% load static %}
this is required before using static tags

[postgresql]
port 5432
dbpwd Kalpav...$ha
pip install psycopg2
pip install psycopg2-binary
{add postgres stuff to btre\settings.py}
python manage.py migrate
python manage.py runserver 8080 --> no migration messages

DB Schema
MODEL/DB FIELDS
### LISTING 
id: int 
realtor: int (foreign key [realtor])
title: str 
address: str 
city: str 
state: str 
zipcode: str 
description: text 
price: int 
bedrooms: int
bathrooms: int 
garage: int [0]
sqft: int 
lot_size: float 
is_published: bool [true]
list_date: date 
photo_main: str 
photo_1: str 
photo_2: str 
photo_3: str 
photo_4: str 
photo_5: str 
photo_6: str 

### REALTOR 
id: int 
name: str 
photo: str 
description: text 
email: str 
phone: str 
is_mvp: bool [0]

python manage.py makemigrations -- creates the files to prepare the migrations to Dbase
pip install Pillow -- for imagefield used in models
python manage.py sqlmigrate listings 0001 -- to view the sql [optional]
    create table app_model(models.py > class Listing) == listings_listing 
python manage.py migrate -- execute the sql


(venv) >python manage.py createsuperuser
Yeon 
yeon.yi@bigpond.com
N02$tates

### CONTACT 
id: int 
user_id: int 
listing: int 
listing_id: int 
name: str 
email: str 
phone: str 
message: text 
contact_date: date 


[push to github]
https://github.com/VY109/btre_project
