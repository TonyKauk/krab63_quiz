from django.db import models
from users.models import User


class Quiz(models.Model):
    """Модель Теста для объединения набора вопросов."""
    name = models.TextField(max_length=100, verbose_name='Название теста')

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return f'Тест {self.name}'


class Question(models.Model):
    """Модель вопроса с привязкой к Тесту."""
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='questions',
    )
    text = models.TextField(max_length=250, verbose_name='Вопрос')
    options = models.ManyToManyField(
        'Option', related_name='questions',
    )

    class Meta:
        verbose_name = 'Вопрос к тесту'
        verbose_name_plural = 'Вопросы к тестам'
        ordering = ['quiz', 'id']

    def __str__(self):
        return f'{self.text[:50]}'


class Option(models.Model):
    """Модель Варианта ответа на вопрос с привязкой к Вопросу."""
    text = models.TextField(max_length=250, verbose_name='Вариант')
    is_correct = models.BooleanField(verbose_name='Верный ответ')

    class Meta:
        verbose_name = 'Вариант ответа на вопрос'
        verbose_name_plural = 'Варианты ответов на вопросы'
        ordering = ['id']

    def __str__(self):
        return f'{self.text}'


class QuizResult(models.Model):
    """Модель для сохранения результатов Теста."""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='quiz_results',
    )
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='quiz_results',
    )
    is_finished = models.BooleanField(
        default=False, editable=False,
        verbose_name='Есть ответы на все вопросы',
    )
    total_questions_count = models.IntegerField(
        default=0, editable=False, verbose_name='Количество вопросов в тесте',
    )
    correct_answers_count = models.IntegerField(
        default=0, editable=False,
        verbose_name='Количество правильных ответов',
    )
    correct_answer_ratio = models.FloatField(
        default=0, editable=False, verbose_name='Процент правильных ответов',
    )

    def save(self, *args, **kwargs):
        if self.is_finished is True:
            self.total_questions_count = self.quiz.questions.count()
            self.correct_answers_count = self.question_results.filter(
                is_correct=True
            ).count()
            if self.correct_answers_count > 0:
                self.correct_answer_ratio = (
                    self.correct_answers_count / self.total_questions_count
                ) * 100
        super(QuizResult, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Результат пройденного теста'
        verbose_name_plural = 'Результаты пройденных тестов'
        ordering = ['id']

    def __str__(self):
        return f'Results of {self.quiz.name}'


class QuestionResult(models.Model):
    """Модель для сохранения результата ответа на вопрос."""
    quiz_result = models.ForeignKey(
        QuizResult, on_delete=models.CASCADE, related_name='question_results',
    )
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='question_results',
    )
    answers = models.ManyToManyField(
        Option, related_name='question_results', blank=True, null=True,
    )
    is_correct = models.BooleanField(
        default=False, editable=False, verbose_name='Ответ верный'
    )

    def correct_answer(self):
        correct_answers = Option.objects.filter(
            questions=self.question, is_correct=True,
        )
        recived_answers = self.answers.all()
        if set(correct_answers) == set(recived_answers):
            self.is_correct = True

    class Meta:
        verbose_name = 'Результат ответа на вопрос'
        verbose_name_plural = 'Результаты ответов на вопросы'
        ordering = ['id']

    def __str__(self):
        return f'Results of {self.question}'
