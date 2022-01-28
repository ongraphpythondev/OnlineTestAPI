from django.contrib import admin
from exam.models import Exam_Detail, MCQ, Solution, Exam_Schedule,Option
# Register your models here.

@admin.register(Exam_Detail)
class ExamDetailAdmin(admin.ModelAdmin):
    list_display=['name','info','duration']

@admin.register(Exam_Schedule)
class ExamScheduleAdmin(admin.ModelAdmin):
    list_display=['exam','start_time']
    
@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display=['exam','question','answer']
    
@admin.register(MCQ)
class MCQAdmin(admin.ModelAdmin):
    list_display=['question','option']



@admin.register(Option)
class MCQAdmin(admin.ModelAdmin):
    list_display=['option1','option2','option3','option4']

