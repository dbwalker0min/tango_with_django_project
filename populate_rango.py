import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import *

data = [
    {
        'Name': 'Python',
        'Pages': [
            {'title': 'Official Python Tutorial', 'url': 'http://docs.python.org/3/tutorial/'},
            {'title': 'How to Think like a Computer Scientist', 'url': 'http://www.greenteapress.com/thinkpython/'},
            {'title': 'Learn Python in 10 Minutes', 'url': 'http://www.korokithakis.net/tutorials/python/'},
        ]
    },
    {
        'Name': 'Django',
        'Pages': [
            {'title': 'Official Django Tutorial', 'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
            {'title': 'Django Rocks', 'url': 'http://www.djangorocks.com/'},
            {'title': 'How to Tango with Django', 'url': 'http://www.tangowithdjango.com/'}
        ]

    },
    {
        'Name': 'Other Frameworks',
        'Pages': [
            {'title': 'Bottle', 'url': 'http://bottlepy.org/docs/dev/'},
            {'title': 'Flask',  'url': 'http://flask.pocoo.org'}
        ]
    }
]


def add_page(category, title, url, views=0):
    p = Page.objects.get_or_create(category=category, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_category(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes = likes
    c.views = views
    c.save()
    return c


def populate():
    global views, likes
    for c in data:
        views = random.uniform(0, 111)
        likes = random.uniform(0, views)
        cat = add_category(c['Name'], likes=likes, views=views)
        for p in c['Pages']:
            add_page(cat, p['title'], p['url'], views=random.uniform(0, 100))


if __name__ == '__main__':
    populate()


