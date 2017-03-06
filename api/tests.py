from django.test import TestCase
from django.urls import reverse

from api.models import keyvalue 
from api.serializers import KeyValueSerializer

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

# Create your tests here.
class TestGetValueByKey(APITestCase):

    def test_get_value_valid_key(self):

        client = APIClient()

        response = client.get('/object/helloworld')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_value_valid_key_with_timestamp(self):
        
        client = APIClient()

        response = client.get('/object/LorenIpsum?timestamp=1488808289')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_value_invalid_key(self):

        client = APIClient()

        response = client.get('/object/helloworld3')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_value_valid_key_with_timestamp(self):
        
        client = APIClient()

        response = client.get('/object/LorenIpsum?timestamp=1488808292')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class TestPostValueByKey(APITestCase):

    def test_post_value(self):

        client = APIClient()

        url = reverse('post_keyvalue')

        post_params = {"testkey":"test key value 1 2 3 4 5 6 7 8 9 0"}

        response = client.post(url, post_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_value_emptyset(self):
    
        client = APIClient()

        url = reverse('post_keyvalue')

        post_params = {}

        response = client.post(url, post_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)


    def test_post_value_match_timestamp(self):

        client = APIClient()

        url = reverse('post_keyvalue')

        post_params = {"testkey":"test key value 1 2 3 4 5 6 7 8 9 0"}

        response = client.post(url, post_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)