from django.urls import path

from api import views

app_name = 'api'


urlpatterns = [
    path(
        'answers/<int:question_id>',
        views.get_correct_answers, name='correct_answers',
    ),
]
