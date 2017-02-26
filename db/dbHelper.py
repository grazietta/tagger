import os
import django
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_settings.settings")
django.setup()
from db.models import * # Must go after django.setup()

# Flight
def create_flight(location, reference_altitude, intrinsic_matrix, date=datetime.datetime.now().date()):
    img_path = '{} - {}'.format(location, date)
    f = Flight(location=location, reference_altitude=reference_altitude, date=date, img_path=img_path, intrinsic_matrix=intrinsic_matrix)
    f.save()
    return f

def delete_flight(flight):
    flight.delete()

def get_all_flights():
    flights = {}
    for f in Flight.objects.all():
        flights[f.location + " " + str(f.date)] = f
    return flights

# Image

# Tag
def create_tag(type, subtype, symbol, num_occurrences=0):
    t = Tag(type=type, subtype=subtype, symbol=symbol, num_occurrences=num_occurrences)
    t.save()
    return t

def delete_tag(tag):
    tag.delete()

def get_all_tags():
    list = []
    for t in Tag.objects.all():
        list.append(t)
    return list

# Marker

if __name__=="__main__":

    # Usage example
    my_tags = get_all_tags()
    print my_tags

    f = create_flight('SFU Surrey', 123, 'my_matrix')
    print f.__dict__
    delete_flight(f)
