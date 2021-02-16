from rest_framework import viewsets
from .models import Eassay, Album, Files
from .serializers import EassaySerializer, AlbumSerializer, FilesSerializer
from rest_framework.filters import SearchFilter

class PostViewSet(viewsets.ModelViewSet):
    queryset = Eassay.objects.all()
    serializer_class = EassaySerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            if self.request.user.username != 'admin':
                qs = qs.filter(author = self.request.user)
        else:
            qs = qs.none()
        return qs

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class FileViewSet(viewsets.ModelViewSet):  
    queryset = Files.objects.all()
    serializer_class = FilesSerializer