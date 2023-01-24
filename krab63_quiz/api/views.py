from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.serializers import OptionSerializer
from quizes.models import Question, Option


@api_view(http_method_names=['GET'])
def get_correct_answers(request, question_id):
    """Функция возвращающая правильные ответы на вопрос."""
    question = Question.objects.get(id=question_id)
    correct_answers = Option.objects.filter(
        questions=question, is_correct=True,
    )
    serializer = OptionSerializer(correct_answers, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)
