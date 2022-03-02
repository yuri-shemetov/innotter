from rest_framework import serializers
from . import models

class PageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = models.Page
        fields = [
            'id', 
            'owner', 
            'name', 
            'description', 
            'tag', 
            'image', 
            'is_private', 
            'followers', 
            'follow_requests', 
            'unblock_date',
            'created_at',
            'updated_at',
            'posts',
        ]
