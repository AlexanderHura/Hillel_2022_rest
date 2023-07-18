from django.http import JsonResponse

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import PostSerializer

from .models import Post


class PostsListApi(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


"In this case in the brouser doesn't it work. I don't know why."
class PostRetriveUpdateDestroyApi(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "id"




