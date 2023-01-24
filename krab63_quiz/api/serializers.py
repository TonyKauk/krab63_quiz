from rest_framework import serializers

from quizes.models import Quiz, Question, Option


# class QuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = ['id', 'text']


# class QuizSerializer(serializers.ModelSerializer):
#     question = QuestionSerializer()

#     class Meta:
#         model = Quiz
#         fields = ['id', 'name', 'question']


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text']
