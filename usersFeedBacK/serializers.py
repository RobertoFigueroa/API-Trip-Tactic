from rest_framework import serializers

from usersFeedBacK.models import UserFeedback
from users.serializers import UserSerializer
from places.serializers import PlaceSerializer

class UserFeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFeedback
        fields=(
	    'id',
            'comment',
            'score',
            'user_id',
            'place'
        )
