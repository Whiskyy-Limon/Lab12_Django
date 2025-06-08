from django.contrib import admin
from .models import Quiz, Question, Choice
from .models import Category, Series

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Category)
admin.site.register(Series)