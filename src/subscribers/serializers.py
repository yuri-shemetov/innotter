from rest_framework import serializers
from users.models import User
from .models import Subscriber


class SubscriberUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = [
            'id',
            'subscriber',
            'follower',
            'follow_requests',
        ]
