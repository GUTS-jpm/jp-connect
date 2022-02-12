import os
import sys

print (sys.path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jpconnect_project.settings')

import django
django.setup()

from jpconnect.models import Employees

def populate():
    add_employee(first_name="John",
                 last_name="Doe",
                 id="0937298",
                 location="Berlin, Germany")
    add_employee(first_name="Ella",
                 last_name="Stone",
                 id="4532294",
                 location="Split, Croatia")
    add_employee(first_name="Steve",
                 last_name="Andrews",
                 id="2053241",
                 location="Glasgow, Scotland")
    add_employee(first_name="Benedict",
                 last_name="Ham",
                 id="1246832",
                 location="Paris, France")
    add_employee(first_name="Sara",
                 last_name="Litterman",
                 id="2033499",
                 location="New York, USA")
    add_employee(first_name="James",
                 last_name="Smith",
                 id="5425647",
                 location="Hong Kong, China")
    add_employee(first_name="Susan",
                 last_name="Mitchel",
                 id="9234554",
                 location="Stockholm, Sweden")
    add_employee(first_name="Micheal",
                 last_name="Scott",
                 id="2345434",
                 location="Madrid, Spain")
    add_employee(first_name="Charlotte",
                 last_name="Moor",
                 id="4542104",
                 location="Geneva, Switzerland")



    for e in Employees.objects.all():
        print(e)

def add_employee(first_name, last_name, id, location):
    e = Employees.objects.get_or_create(id=id)[0]
    e.first_name = first_name
    e.last_name = last_name
    e.location = location
    e.save()
    return e

if __name__ == "__main__":
    print("Starting populating script")
    populate()
