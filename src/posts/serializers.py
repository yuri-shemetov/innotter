from rest_framework import serializers
from .models import Post
from likes import services as likes_services

class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'page', 'content', 'is_fan', 'total_likes',)

    def get_is_fan(self, obj) -> bool:
        """Проверяет, лайкнул ли `request.user` картинку (`obj`).
        """
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)