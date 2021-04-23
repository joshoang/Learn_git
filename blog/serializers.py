from rest_framework import serializers
from .models import Post

class GetAllPostSerializer (serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','body')

class PostPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 100,required=True)
    body =  serializers.CharField()
