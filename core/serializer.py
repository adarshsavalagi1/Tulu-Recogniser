from rest_framework import serializers
from PIL import Image

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()
