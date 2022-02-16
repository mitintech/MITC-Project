from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(tbl_student)
admin.site.register(tbl_teacher)
admin.site.register(tbl_question)
admin.site.register(tbl_result)
admin.site.register(tbl_practicalquestions)