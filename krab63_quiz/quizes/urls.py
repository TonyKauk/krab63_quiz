from django.urls import path

from . import views

app_name = 'quizes'


urlpatterns = [
    path('', views.QuizListView.as_view(), name='quizes_list'),
    path('<int:quiz_id>/welcome/', views.quiz_welcome, name='quiz_welcome'),
    path(
        '<int:quiz_id>/<int:question_id>',
        views.quiz_question, name='quiz_question',
    ),
    path(
        'answers/<int:quiz_id>/<int:question_id>',
        views.get_correct_answers, name='correct_answers',
    ),
    path(
        '<int:quiz_id>/results/',
        views.quiz_results, name='quiz_results',
    ),
]
