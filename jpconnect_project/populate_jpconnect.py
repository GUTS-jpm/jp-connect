import os
import sys

print (sys.path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jpconnect_project.settings')

import django
django.setup()

from jpconnect.models import Employee

def populate():
    add_employee(first_name="John",
                 last_name="Doe",
                 id="0937298",
                 location="Germany,Berlin")
    add_employee(first_name="Ella",
                 last_name="Higgins",
                 id="4532294",
                 location="Split,Croatia")
    add_employee(first_name="Steve",
                 last_name="Andrews",
                 id="2053241",
                 location="Scotland,Glasgow")


    for e in Employee.objects.all():
        print(e)

def add_employee(first_name, last_name, id, location):
    e = Employee.objects.get_or_create(id=id)[0]
    e.first_name = first_name
    e.last_name = last_name
    e.location = location
    e.save()
    return e

if __name__ == "__main__":
    print("Starting populating script")
    populate()
