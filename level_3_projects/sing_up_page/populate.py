import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'level_2_test_project.settings')

import django
django.setup()

import random
from main_app.models import User
from faker import Faker

fake_data = Faker()

def fake_data_gen(num=5):
    for _ in range(num):
        fake_first_name = fake_data.first_name()
        fake_last_name = fake_data.last_name()
        fake_email = fake_data.email()

        users = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]


if __name__ == "__main__":
    print('Populating')
    fake_data_gen(12)
    print('Done!')
