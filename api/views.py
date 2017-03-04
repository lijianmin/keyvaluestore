from django.shortcuts import render

from api.models import keyvalue
from api.serializers import KeyValueSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from keyvaluestore.database import *

from datetime import *

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

            # process the loaded json - well, since the json has unpredictable field names :)
            for k in parsed_data:
                key = k
                value = parsed_data[k]

            # get collection
            keyvalueCollection = database().getCollection("keyvalue")

            # insert key : value into database
            # pending auto generation of timestamp (epoch based)
            timeOfInsert = datetime.utcnow()

            keyvalueCollection.insert_one({ "key" : key, "value" : value, "timestamp" : int(timeOfInsert.strftime('%s')) })

            # return Response
            return Response("Time: " + str(timeOfInsert.strftime('%I:%M %p')), status=status.HTTP_200_OK)
            
        except:
            
            # nothing found HTTP 404
            return Response({
                        "status" : status.HTTP_500_INTERNAL_SERVER_ERROR,
                        "message" : "Error encountered while processing data"
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class get_keyvalue (APIView):
       
    def get(self, request, key, format=None):
        
        """
            By key and (optional) timestamp
            
            Either 1) /object/<key>
            or     2) /object/<key>?timestamp=<timestamp>

            If timestamp is not specified, latest entry matching the key will be returned
            Else return entry matching both key and timestamp
        """ 

        try:
        
            # Optional parameter: timestamp
            timestamp = request.GET.get("timestamp")

            # Get collection
            keyvalueCollection = database().getCollection("keyvalue")

            # Form query
            if timestamp is None:
                query = { "key" : key }
            else:
                query = { "key" : key, "timestamp" : int(timestamp) }
   
            # get value based on key
            # then sort in descending order of timestamp to get the record with the latest timestamp
            keyvalue = keyvalueCollection.find(query).sort([("timestamp",-1)])

            # return response of keyvalue index 0 with HTTP 200 OK status
            return Response({ "value" : keyvalue[0]["value"] }, status=status.HTTP_200_OK)

        except:
            
            # nothing found HTTP 404
            return Response({
                        "status" : status.HTTP_404_NOT_FOUND,
                        "message" : "Result not found"
                    }, status=status.HTTP_404_NOT_FOUND)