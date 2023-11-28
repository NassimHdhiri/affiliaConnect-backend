# init_db.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from affiliates.models import UserProfile

profiles = [
    {
      'id': 1,
      'firstName': 'John',
      'lastName': 'Doe',
      'age':25,
      'trackingLink':"www.google.com/users",
      'webSite':"www.nassim.com",
      'field': 'health',
      'commPref': 'email',
      'methodOfPayment': 'paypal',
      'etc': 'other details',
      'gender':'male',
      'commRate': 15,
      'location': 'Tunis',
      'tel': '50962823',
      'email': 'john.doe@example.com',
      'imagePath': 'https://source.unsplash.com/featured/?person',
      'experience':3

    },
    {
      'id': 2,
      'firstName': 'Jane',
      'lastName': 'Smith',
      'age':25,
      'trackingLink':"www.google.com/users",
      'webSite':"www.nassim.com",
      'gender':'male',
      'field': 'IT',
      'commPref': 'Phone',
      'methodOfPayment': 'Credit_Card',
      'etc': 'other details',
      'commRate': 12,
      'location': 'Sfax',
      'tel': '50962823',
      'email': 'jane.smith@example.com',
      'imagePath': 'https://source.unsplash.com/featured/?friend',
      'experience':3

    },
    {
      'id': 3,
      'firstName': 'Michael',
      'lastName': 'Johnson',
      'age':25,
      'trackingLink':"www.google.com/users",
      'webSite':"www.nassim.com",
      'gender':'male',
      'field': 'Marketing',
      'commPref': 'Slack',
      'methodOfPayment': 'Bitcoin',
      'etc': 'other details',
      'commRate': 18,
      'location': 'Ariana',
      'tel': '50962823',
      'email': 'michael.johnson@example.com',
      'imagePath': 'https://source.unsplash.com/featured/?single',
      'experience':3

    },
    {
      'id': 4,
      'firstName': 'Emily',
      'lastName': 'Brown',
      'gender':'male',
      'age':25,
      'trackingLink':"www.google.com/users",
      'webSite':"www.nassim.com",
      'field': 'Marketing',
      'commPref': 'email',
      'methodOfPayment': 'Venmo',
      'etc': 'other details',
      'commRate': 10,
      'location': 'Sfax',
      'tel': '50962823',
      'email': 'emily.brown@example.com',
      'imagePath': 'https://source.unsplash.com/featured/?europe',
      'experience':3

    },
    {
      'id': 5,
      'firstName': 'Alex',
      'lastName': 'Garcia',
      'gender':'male',
      'age':25,
      'trackingLink':"www.google.com/users",
      'webSite':"www.nassim.com",
      'field': 'Clothes',
      'commPref': 'Phone',
      'methodOfPayment': 'credit-card',
      'etc': 'other details',
      'commRate': 14,
      'location': 'Sousse',
      'tel': '50962823',
      'email': 'alex.garcia@example.com',
      'imagePath': 'https://source.unsplash.com/featured/?marketing',
      'experience':3

    },
    {
      'id': 6,
      'firstName': 'Sophia',
      'lastName': 'Lee',
      'age':25,
      'trackingLink':"www.google.com/users",
      'webSite':"www.nassim.com",
      'gender':'male',
      'field': 'Foods',
      'commPref': 'email',
      'methodOfPayment': 'paypal',
      'etc': 'other details',
      'commRate': 16,
      'location': 'Jerjis',
      'tel': '50962823',
      'email': 'sophia.lee@example.com',
      'imagePath': 'https://source.unsplash.com/featured/?persona',
      'experience':3

    },
    {
      'id': 7,
      'firstName': 'Elijah',
      'lastName': 'Wang',
      'age':25,
      'trackingLink':"www.google.com/users",
      'webSite':"www.nassim.com",
      'gender':'male',
      'field': 'Clothes',
      'commPref': 'Slack',
      'methodOfPayment': 'Bitcoin',
      'etc': 'other details',
      'commRate': 20,
      'location': 'Kef',
      'tel': '50962823',
      'email': 'elijah.wang@example.com',
      'imagePath': 'https://source.unsplash.com/featured/?avatar',
      'experience':3

    },
    {
      'id': 8,
      'firstName': 'Olivia',
      'lastName': 'Martinez',
      'age':25,
      'trackingLink':"www.google.com/users",
      'webSite':"www.nassim.com",
      'gender':'male',
      'field': 'Foods',
      'commPref': 'Phone',
      'methodOfPayment': 'Venmo',
      'etc': 'other details',
      'commRate': 13,
      'location': 'Jandouba',
      'tel': '50962823',
      'email': 'olivia.martinez@example.com',
      'imagePath': 'https://source.unsplash.com/featured/?child',
      'experience':3

    },
    {
      'id': 9,
      'firstName': 'Liam',
      'lastName': 'Taylor',
      'age':25,
      'trackingLink':"www.google.com/users",
      'webSite':"www.nassim.com",
      'gender':'male',
      'field': 'Marketing',
      'commPref': 'email',
      'methodOfPayment': 'Credit_Card',
      'etc': 'other details',
      'commRate': 11,
      'location': 'Sfax',
      'tel': '50962823',
      'email': 'liam.taylor@example.com',
      'imagePath': 'https://source.unsplash.com/featured/?developer',
      'experience':3

    },
    {
      'id': 10,
      'firstName': 'Ava',
      'age':25,
      'trackingLink':"www.google.com/users",
      'webSite':"www.nassim.com",
      'gender':'male',
      'lastName': 'Nguyen',
      'field': 'IT',
      'commPref': 'Slack',
      'methodOfPayment': 'paypal',
      'etc': 'other details',
      'commRate': 17,
      'location': 'Ariana',
      'tel': '50962823',
      'email': 'ava.nguyen@example.com',
      'imagePath': 'https://source.unsplash.com/featured/?men',
      'experience':3

    },
    {
      'id': 11,
      'firstName': 'Logan',
      'lastName': 'Anderson',
      'age':25,
      'trackingLink':"www.google.com/users",
      'webSite':"www.nassim.com",
      'gender':'male',
      'field': 'health',
      'commPref': 'email',
      'methodOfPayment': 'Bitcoin',
      'etc': 'other details',
      'commRate': 19,
      'location': 'Sousse',
      'tel': '54011448',
      'email': 'logan.anderson@example.com',
      'imagePath': 'https://source.unsplash.com/featured/?woamen',
      'experience':3
    },
    {
      'id': 12,
      'firstName': 'Mia',
      'lastName': 'Davis',
      'age':25,
      'trackingLink':"www.google.com/users",
      'webSite':"www.nassim.com",
      'gender':'male',
      'field': 'Clothes',
      'commPref': 'Phone',
      'methodOfPayment': 'Venmo',
      'etc': 'other details',
      'commRate': 12,
      'location': 'Tunis',
      'tel': '12345678',
      'email': 'mia.davis@example.com',
      'imagePath': 'https://source.unsplash.com/featured/?male',
      'experience':3
    },
]

for profile_data in profiles:
    UserProfile.objects.create(**profile_data)

print('Database initialization completed.')
