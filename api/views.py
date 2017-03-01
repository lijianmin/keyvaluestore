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
        
    def get(self, request, format=None):
