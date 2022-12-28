from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from quizes.models import QuizResult
from .forms import CreationForm


class SignUp(CreateView):
    """Класс для регистрации новых пользователей."""
    form_class = CreationForm
    success_url = reverse_lazy('quizes:quizes_list')
    template_name = 'users/signup.html'


@login_required
def my_profile(request):
    """Функция для отображения результатов пройденных тестов в личном кабинете
    пользователя.
    """
    results = QuizResult.objects.filter(user=request.user, is_finished=True)
    context = {'results': results}
    template = 'users/my_profile.html'
    return render(request, template, context)
