from django.db import models

# Create your models here.
class keyvalue (object):
    def __init__(self, key, value, timestamp):
        self.key = key
        self.value = value
        self.timestamp = timestamp