from django import forms
from django.forms import ValidationError

from .models import Option, Question, QuestionResult


class QuestionResultForm(forms.ModelForm):
    """Форма для модели QuestionResult."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answers'].queryset = Option.objects.filter(
            questions=self.instance.question
        )

    answers = forms.ModelMultipleChoiceField(
        queryset=None, to_field_name='text',
        widget=forms.CheckboxSelectMultiple,
        label='Варианты ответа на вопрос', required=False,
    )

    class Meta:
        model = QuestionResult
        fields = ['answers']

    def clean_answers(self):
        data = self.cleaned_data['answers']
        count_recieved_answers = len(data)
        count_all_answers = self.instance.question.options.all().count()
        if count_recieved_answers == 0:
            raise ValidationError('Необходимо выбрать хотя бы один вариант')
        if count_recieved_answers == count_all_answers:
            raise ValidationError('Нельзя выбирать все варианты сразу')
        return data


class QuestionAdminForm(forms.ModelForm):
    """Форма для создания вопросов через админку."""
    options = forms.ModelMultipleChoiceField(
        queryset=Option.objects.all(), required=False,
    )

    class Meta:
        model = Question
        fields = ['text', 'options', 'quiz']

    def clean_options(self):
        data = self.cleaned_data['options']
        count_recieved_options = len(data)
        count_correct_options = data.filter(is_correct=True).count()
        if count_correct_options == count_recieved_options:
            raise ValidationError(
                'Добавьте как минимум один неправильный вариант'
            )
        if count_correct_options == 0:
            raise ValidationError(
                'Добавьте как минимум один правильный вариант'
            )
        return data
