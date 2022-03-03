from rest_framework import serializers
from .models import Post
from likes import services as likes_services


class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()
    total_likes = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'page', 'content', 'is_fan', 'total_likes',)

    def get_is_fan(self, obj) -> bool:
        """Checking `like` from `request.user` for (`obj`).
        """
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)

    def get_total_likes(self, obj) -> int:
        """Count `like` from `request.user` for (`obj`).
        """
        return likes_services.get_count_fans(obj)