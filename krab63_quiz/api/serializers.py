from rest_framework import serializers

from quizes.models import Option


class OptionSerializer(serializers.ModelSerializer):
    """Сериализатор для отаетов на вопросы."""
    class Meta:
        model = Option
        fields = ['id', 'text']
