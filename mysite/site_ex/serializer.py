from rest_framework import serializers
from .models import *

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username']


class FollowSerializer(serializers.ModelSerializer):
    follower_user = UserProfileSerializer()
    following_user = UserProfileSerializer()
    class Meta:
        model = Follow
        fields = ['follower_user', 'following_user', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'image', 'video', 'description', 'hashtag', 'created_at']


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['post', 'user', 'text', 'created_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'user', 'text', 'parent', 'created_at']


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ['user', 'comment', 'like', 'created_at']


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['user', 'image', 'video', 'created_at']


class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Save
        fields = '__all__'


class SaveItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaveItem
        fields = '__all__'