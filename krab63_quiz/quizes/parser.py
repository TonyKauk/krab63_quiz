import random

import requests
from bs4 import BeautifulSoup

from quizes.models import Quiz, Question, Option


def get_soup(url):
    """Создает объект класса BeautifulSoup со страницей, которая доступной по
    указанному URL.
    """
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")


def get_quiz(soup):
    """Получаем/создаем объект класса Тест."""
    quiz_name = soup.find('h1').string
    quiz, created = Quiz.objects.get_or_create(name=quiz_name)
    if created:
        quiz.save()
    return quiz


def question_to_be_imported(soup, quiz):
    """Проверяем есть ли уже такой вопрос в базе и сохраняем если нет."""
    question_elements = soup.find_all('div', class_='test_t')
    for question in question_elements:
        if question.find('b'):
            question_text = question.find('b').string
            if not Question.objects.filter(text=question_text).exists():
                question_object = Question.objects.create(
                    quiz=quiz, text=question_text,
                )
                question_object.save()
                return question_object, question
    return None


def get_options(question_object, question):
    """Получаем все варианты ответа к интересующему вопросу."""
    options = question.find_all('span')
    texts = []
    is_corrects = []
    for option in options:
        option_text = option.text
        texts.append(option_text)
        if not is_corrects:
            is_corrects.append(True)
        elif len(is_corrects) == 1:
            is_corrects.append(False)
        else:
            is_corrects.append(random.choice([True, False]))
    for text, is_correct in zip(texts, is_corrects):
        new_option = Option.objects.create(text=text, is_correct=is_correct)
        question_object.options.add(new_option)
    pass


def parser():
    """Основная функция выполняющая парсинг."""
    URL = 'https://centrevraz.ru/dlya-rvp-vnzh'

    soup = get_soup(URL)
    quiz = get_quiz(soup)
    question = question_to_be_imported(soup, quiz)
    if question:
        get_options(question[0], question[1])
    pass
