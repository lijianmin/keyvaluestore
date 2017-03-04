from django.shortcuts import render

from api.models import keyvalue
from api.serializers import KeyValueSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from keyvaluestore.database import *

import json

# Create your views here.
class post_keyvalue (APIView):
    
    """
        Accepts JSON
        {
            "key" : "value",
        }
    """
    
    def post(self, request, format=None):
        
        """
            Insert or update a key-value object
            
            If key exists -> "update" with timestamp (insert new row)
            else if key does not exist -> insert new row with timestamp
        """
        
        try:

            # load json from payload 
            parsed_data = request.data

            # process the loaded json
            for k in parsed_data:
                key = k
                value = parsed_data[k]

            # get collection
            keyvalueCollection = database().getCollection('keyvalue')

            # insert key : value into database
            # pending auto generation of timestamp (epoch based)
            keyvalueCollection.insert_one({ 'key' : key, 'value' : value })

            # return Response
            return Response(status=status.HTTP_200_OK)
            
        except:
            
            # nothing found HTTP 404
            return Response({
                        "error" : {
                                "status" : status.HTTP_500_INTERNAL_SERVER_ERROR,
                                "message" : "ERROR"
                        }
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class get_keyvalue (APIView):
       
    def get(self, request, format=None):
        
        """
            By key and (optional) timestamp
            
            Either 1) /object/<key>
            or     2) /object/<key>?timestamp=<timestamp>
        """

        try:
            # optional parameter named timestamp
            timestamp = int(request.data['timestamp'])

            # get collection
            keyvalueCollection = database().getCollection('keyvalue')

            # form query
            query = { "key" : request.GET['key'] }
            
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
