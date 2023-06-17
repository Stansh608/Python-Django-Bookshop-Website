from django.contrib import admin

# Register your models here.

#Register Question
from .models import Question
admin.site.register(Question)
