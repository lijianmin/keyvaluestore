from django.shortcuts import render
from django.views.decorator.csrf import csrf_exempt

from api.models import keyvalue
from api.serializers import KeyValueSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from keyvaluestore.database import *

# Create your views here.
class keyvalue (APIView):
    
    def post(self, request, format=None):
        # insert or update a key-value object
        # if key exists -> "update" with timestamp (insert new row)
        # else if key does not exist -> insert new row with timestamp

    def get(self, request, format=None):
        # by key and (optional) timestamp
        # either 1) /object/<key>
        # or     2) /object/<key>?timestamp=<timestamp>

        try:
            # optional parameter named timestamp
            timestamp = int(request.data['timestamp'])

            # get collection
            keyvalueCollection = database().getCollection('keyvalue')

            # form query
            query = { "key" : key }
            
            # get value based on key (return the one with the latest timestamp)
            # descending order of timestamp - we want the latest
            keyvalue = keyvalueCollection.find(query).sort({ "timestamp":-1 })[0]

            # return response w/ HTTP 200
            return Response(keyvalue['value'], status=status.HTTP_200_OK)

        except:
            
            # nothing found HTTP 404
            return Response({
                        "error" : {
                                "status" : status.HTTP_404_NOT_FOUND,
                                "message" : "Result not found"
                        }
                    }, status=status.HTTP_404_NOT_FOUND)
