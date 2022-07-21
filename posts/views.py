from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "id"

    def retrieve(self, request, id):
        product = Product.objects.get(id=id)
        product.views = F('views_count') + 1
        product.save()
        return super().retrieve(request, id)
