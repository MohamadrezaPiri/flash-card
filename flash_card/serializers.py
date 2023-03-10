from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import FlashCard


class CreateUserProfileSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'password']


class CreateFlashCardSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = FlashCard
        fields = ['id', 'user_id', 'question', 'answer']

    def save(self):
        user_id = self.context['user_id']
        question = self.validated_data['question']
        answer = self.validated_data['answer']

        FlashCard.objects.create(
            user_id=user_id, question=question, answer=answer)
