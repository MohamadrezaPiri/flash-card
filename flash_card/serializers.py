from djoser.serializers import UserCreateSerializer
from rest_framework.serializers import ModelSerializer
from .models import FlashCard


class CreateUserProfileSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'password']


class CreateFlashCardSerializer(ModelSerializer):
    class Meta:
        model = FlashCard
        fields = '__all__'
