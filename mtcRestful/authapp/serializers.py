
from rest_framework import serializers
from mainapp.models import Toy
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Переводим нашу структуру(Пользователя) в последовательность битов."""

    toys = serializers.PrimaryKeyRelatedField(many=True,
                                              queryset=Toy.objects.all())

    class Meta:
        model = User
        field = '__all__'
