from stats.packages.base import PackageBuilder
from haystack.query import SearchQuerySet
from django.contrib.gis.geos import Point


class LocationDetailsPackageBuilder(PackageBuilder):

    def __init__(self, latitude, longitude):
        self.longitude = longitude
        self.latitude = latitude

    def get_objects(self):
        location = Point(float(self.longitude), float(self.latitude))
        objects = SearchQuerySet().within('location', location, location).facet('ip').facet_counts()
        return objects['fields']['ip']

    def render_each_object(self, each_object):
        template = '["{0}","{1}","{2}",{3}]'
        this_object = SearchQuerySet().filter(ip=each_object[0])
        latest_attack = this_object.latest('timestamp')
        count = each_object[1]
        timestamp = latest_attack.timestamp.isoformat()
        return template.format(latest_attack.attacked_service, latest_attack.ip, timestamp, count)