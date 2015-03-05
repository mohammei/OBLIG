from django.contrib import admin
from polls.models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question)
# Register your models here.