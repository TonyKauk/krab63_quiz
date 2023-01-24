from quizes.models import Quiz, Question, Option

import re

import requests
from bs4 import BeautifulSoup

from quizes.models import Quiz, Question, Option


def parser():
    URL = 'https://centrevraz.ru/dlya-rvp-vnzh'

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    quiz_name = soup.find('h1').string
    quiz, created = Quiz.objects.get_or_create(name=quiz_name)
    if created:
        quiz.save()
    print(quiz_name)

    question_elements = soup.find_all('div', class_='test_t')
    for question in question_elements:
        question_text = question.find('b').string
        print(question_text)
        if not Question.objects.filter(text=question_text).exists():
            new_question = Question.objects.create(
                quiz=quiz, text=question_text,
            )
            new_question.save()

        options = question.find_all('label', class_=re.compile('countp-'))
        randomizer = 1
        is_correct = True
        options = []
        for option in options:
            option_text = option.find('span').string
            print(option_text)
            if randomizer > 0:
                randomizer *= -1
                is_correct = True
            else:
                randomizer *= -1
                is_correct = False
            print(is_correct)
            option = Option.objects.create(
                text=option_text, is_correct=is_correct,
            )
            option.save()
            options.append(option)

        new_question.options.add(*options)
    pass
