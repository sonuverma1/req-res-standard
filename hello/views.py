from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class sampleApi(APIView):
    def get(self, request):
        data = {"value": 123}
        return Response(data, 200)

    def post(self, request):
        print("in the api")
        request.data['first'] = "no"
        print(request.data)
        data = {"value": 345}
        return Response(data, 200)


def home(request):
    print(request)
    return HttpResponse("This is new home")
