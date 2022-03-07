from rest_framework import serializers
from users.models import User


class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]
