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
        print(request.body)
        print(request.headers)
        data = {"value": 345}
        return Response(data, 200)


class raiseException(APIView):
    def post(self, request):
        raise Exception("Some error")


def home(request):
    print(request)
    return HttpResponse("This is new home")
