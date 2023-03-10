# Generated by Django 4.1.4 on 2022-12-29 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=250, verbose_name='Вариант')),
                ('is_correct', models.BooleanField(verbose_name='Верный ответ')),
            ],
            options={
                'verbose_name': 'Вариант ответа на вопрос',
                'verbose_name_plural': 'Варианты ответов на вопросы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=250, verbose_name='Вопрос')),
                ('options', models.ManyToManyField(related_name='questions', to='quizes.option')),
            ],
            options={
                'verbose_name': 'Вопрос к тесту',
                'verbose_name_plural': 'Вопросы к тестам',
                'ordering': ['quiz', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, verbose_name='Название теста')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='QuizResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_finished', models.BooleanField(default=False, editable=False, verbose_name='Есть ответы на все вопросы')),
                ('total_questions_count', models.IntegerField(default=0, editable=False, verbose_name='Количество вопросов в тесте')),
                ('correct_answers_count', models.IntegerField(default=0, editable=False, verbose_name='Количество правильных ответов')),
                ('correct_answer_ratio', models.FloatField(default=0, editable=False, verbose_name='Процент правильных ответов')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_results', to='quizes.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_results', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Результат пройденного теста',
                'verbose_name_plural': 'Результаты пройденных тестов',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='QuestionResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False, editable=False, verbose_name='Ответ верный')),
                ('answers', models.ManyToManyField(blank=True, null=True, related_name='question_results', to='quizes.option')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_results', to='quizes.question')),
                ('quiz_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_results', to='quizes.quizresult')),
            ],
            options={
                'verbose_name': 'Результат ответа на вопрос',
                'verbose_name_plural': 'Результаты ответов на вопросы',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quizes.quiz'),
        ),
    ]
