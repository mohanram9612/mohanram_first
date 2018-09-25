from django.shortcuts import render
from polls.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def test_function(request):
    print('test_function')
    return Response({"Key": 'Mohan Ram'})
