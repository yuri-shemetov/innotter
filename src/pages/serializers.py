from rest_framework import serializers
from . import models
from subscribers import services as subscribers_services


class PageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    is_subscriber = serializers.SerializerMethodField()
    is_follow_requests = serializers.SerializerMethodField()

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
            'count_followers',
            'count_follow_requests',
            'unblock_date',
            'created_at',
            'updated_at',
            'posts',
            'is_subscriber',
            'is_follow_requests',
        ]

    def get_is_subscriber(self, obj) -> bool:
        """Checking `subscriber` from `request.user` for (`obj`).
        """
        user = self.context.get('request').user
        return subscribers_services.is_subscriber(obj, user)

    def get_is_follow_requests(self, obj) -> bool:
        """Checking `follow_requests` from `request.user` for (`obj`).
        """
        user = self.context.get('request').user
        return subscribers_services.is_follow_requests(obj, user)
