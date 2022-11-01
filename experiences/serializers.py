from rest_framework import serializers
from .models import Perk, Experience
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer


class PerkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):

    host = TinyUserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    perks = PerkSerializer(many=True, read_only=True)

    class Meta:
        model = Experience
        fields = "__all__"


class ExperienceDetailSerializer(serializers.ModelSerializer):
    pass
