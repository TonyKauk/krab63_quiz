from django.contrib import admin

from .forms import QuestionAdminForm
from .models import Option, Question, Quiz


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    pass


admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
