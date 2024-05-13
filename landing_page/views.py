from django.shortcuts import render
from rest_framework.views import  APIView
from .models import TileModel
from rest_framework.response import Response
from .serializer import TileSerializer
# Create your views here.



class LandingPage(APIView):

    serializer = TileSerializer()


    def get(self, request):
        tiles = TileModel.objects.all()
        return  Response(tiles)