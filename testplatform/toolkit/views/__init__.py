import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView


class TestView(APIView):
    def get(self,request):
        result = {"password": "aaaaaaa", "encrypt": "aaaaaaaaaaaaaaaaaaaa"}
        return HttpResponse(json.dumps(result), content_type="application/json")

    def post(self,request):
        data = JSONParser().parse(request)
        return HttpResponse(json.dumps(data), content_type="application/json")