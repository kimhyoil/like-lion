from .models import Eassay, Album, Files
from rest_framework import serializers

class EassaySerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Eassay
        fields = ('pk', 'title', 'body', 'author_name')

class AlbumSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Album
        fields = ('pk', 'author_name', 'image', 'desc')

class FilesSerializer(serializers.ModelSerializer):
    authorr = serializers.ReadOnlyField(source='author.username')
    file = serializers.FileField(use_url=True)

    class Meta:
        model = Files
        # self 변수 + model에서 정의한 변수명
        fields = ('pk', 'authorr', 'file', 'desc')
