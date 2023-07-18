from rest_framework import serializers

from posts.models import Post

class PostSerializers(serializers.ModelSerializers):
    class Meta:
        model = Post
        fields = "__all__"
