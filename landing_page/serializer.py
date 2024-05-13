from rest_framework import serializers


class TileSerializer(serializers.Serializer):
   title = serializers.CharField(max_length=50)
   description = serializers.CharField(max_length=100)
   image = serializers.ImageField(upload_to='images/', null=True)
   url_link = serializers.URLField(max_length=200, null=True)
   
    