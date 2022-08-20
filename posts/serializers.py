from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import PostModel, Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']
