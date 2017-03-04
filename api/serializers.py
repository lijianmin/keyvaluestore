from rest_framework import serializers
from api.models import keyvalue

class KeyValueSerializer(serializers.Serializer):
    # identifier
    key = serializers.CharField(required=True, min_length=1, max_length=255)
    
    # json blob or string - no length restriction
    value = serializers.CharField(required=True, min_length=1, max_length=None)
    
    # timestamp in UTC (epoch timestamp e.g. 1440568980 which is 6.03PM August 15 2015)
    timestamp = serializers.DateTimeField(required=True, format="%s")