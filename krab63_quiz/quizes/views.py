from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from quizes.forms import QuestionResultForm
from quizes.models import Question, QuestionResult, Quiz, QuizResult


class QuizListView(generic.ListView):
    """Отображает все доступные Тесты."""
    template_name = 'quizes/quizes_list.html'
    context_object_name = 'quizes'

    def get_queryset(self):
        """Возвращает все Тесты."""
        return Quiz.objects.all()


@login_required
def quiz_welcome(request, quiz_id):
    """Возвращает страницу с приветствием и парвилами теста."""
    quiz = Quiz.objects.get(id=quiz_id)
    first_question_id = quiz.questions.first().id

    # Удаляем все предыдущие незавершенные попытки пользователя в данном тесте
    QuizResult.objects.filter(
        quiz=quiz, user=request.user, is_finished=False,
    ).delete()

    context = {
        'quiz': quiz,
        'first_question_id': first_question_id,
    }
    template = 'quizes/quiz_welcome.html'
    return render(request, template, context)


@login_required
def quiz_question(request, quiz_id, question_id):
    """Возвращает страницу со следующим вопросом теста."""
    # Находим запрошенный тест и на его основе находим или создаем запись с
    # результатами данного теста
    quiz = get_object_or_404(Quiz, id=quiz_id)
    quiz_result, created = QuizResult.objects.get_or_create(
        user=request.user, quiz=quiz, is_finished=False,
    )
    if created:
        quiz_result.save()

    # Находим вопрос и на его основе находим или создаем запись с
    # результатами данного вопроса
    question = get_object_or_404(Question, id=question_id)
    option = question.options.all()
    question_result, created = QuestionResult.objects.get_or_create(
        quiz_result=quiz_result, question=question,
        quiz_result__is_finished=False,
    )
    if created:
        question_result.save()

    context = {
                'question': question,
                'options': option,
                'quiz_id': quiz_id,
                'quiz': quiz,
            }
    template = 'quizes/quiz_question.html'

    if request.method == 'POST':
        question_result_form = QuestionResultForm(
            request.POST, instance=question_result,
        )
        if question_result_form.is_valid():
            question_result = question_result_form.save()
        else:
            context['question_result_form'] = question_result_form
            return render(request, template, context)

        next_question = Question.objects.filter(id__gt=question_id).first()
        if next_question is None:
            quiz_result.is_finished = True
            quiz_result.save()
            return redirect('quizes:quiz_results', quiz_id=quiz_id)

        next_question_id = next_question.id
        return redirect(
            'quizes:quiz_question', quiz_id=quiz_id,
            question_id=next_question_id,
        )

    question_result_form = QuestionResultForm(instance=question_result)
    context['question_result_form'] = question_result_form
    return render(request, template, context)


@login_required
def quiz_results(request, quiz_id):
    """Показывает результаты пройденного теста."""
    quiz = Quiz.objects.get(id=quiz_id)
    quiz_result = QuizResult.objects.filter(
        user=request.user, quiz=quiz
    ).last()

    for question_result in quiz_result.question_results.all():
        question_result.correct_answer()
        question_result.save()
    quiz_result.save()
    context = {
        'quiz_result': quiz_result,
        'quiz_name': quiz.name,
    }
    template = 'quizes/quiz_results.html'
    return render(request, template, context)
