"""
WSGI config for krab63_quiz project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Если в папаке проекта есть файл 'settings_local.py', то будут использованы
# его настройки, в противном случае - настройки из 'settings.py'

# file_name = 'settings_local.py'
# cur_dir = os.getcwd()

# file_list = os.listdir(cur_dir)
# if file_name in file_list:
#     os.environ['DJANGO_SETTINGS_MODULE'] = 'krab63_quiz.settings_local'
# else:
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'krab63_quiz.settings')

# dirname = os.path.dirname(__file__)
# relative_path = os.path.join(dirname, 'settings_local.py')
# settings_local_exists = os.path.exists(relative_path)

# if settings_local_exists:
#     os.environ['DJANGO_SETTINGS_MODULE'] = 'krab63_quiz.settings_local'
# else:
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'krab63_quiz.settings')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'krab63_quiz.settings')

application = get_wsgi_application()
