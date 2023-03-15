from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import FlashCard, Category


class CreateUserProfileSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'password']


class FlashCardSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = FlashCard
        fields = ['id', 'user_id', 'category', 'question', 'answer']


class CreateFlashCardSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = FlashCard
        fields = ['id', 'user_id', 'category', 'question', 'answer']

    def save(self):
        user_id = self.context['user_id']
        question = self.validated_data['question']
        answer = self.validated_data['answer']
        category = self.validated_data['category']

        FlashCard.objects.create(
            user_id=user_id, question=question, answer=answer, category=category)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)
