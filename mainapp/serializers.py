from rest_framework import serializers
from mainapp.models import Toy
from django.contrib.auth.models import User


class ToySerializer(serializers.ModelSerializer):
    """Сериализация по игрушкам."""

    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Toy
        fields = '__all__'
        # fields = ('id',
        #           'name',
        #           'owner',
        #           'description',
        #           'toy_category',
        #           'base_material',
        #           'was_included_in_home',)


class UserSerializer(serializers.ModelSerializer):
    """Сериализация по пользователям."""

    toys = serializers.PrimaryKeyRelatedField(many=True, queryset=Toy.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'toys')
