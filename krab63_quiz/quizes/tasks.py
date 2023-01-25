from krab63_quiz.celery import app
from quizes.parser import parser


@app.task
def parse():
    parser()
    pass
