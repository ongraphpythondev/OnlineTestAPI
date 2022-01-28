from django.contrib import admin
from exam.models import Exam_Detail, MCQ, Solution, Exam_Schedule,Option,Question
# Register your models here.

# setting Exam_Detail model in django admin
@admin.register(Exam_Detail)
class ExamDetailAdmin(admin.ModelAdmin):
    
    # after data get saved field(s) in django admin displayed as below format
    list_display=['name','info','duration'] 

# setting Exam_Schedule model in django admin
@admin.register(Exam_Schedule)
class ExamScheduleAdmin(admin.ModelAdmin):
    
    # after data get saved field(s) in django admin displayed as below format
    list_display=['exam','start_time']
    
# setting Solution model in django admin
@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    
    # after data get saved field(s) in django admin displayed as below format
    list_display=['exam','question','answer']

# setting MCQ model in django admin
@admin.register(MCQ)
class MCQAdmin(admin.ModelAdmin):
    
    # after data get saved field(s) in django admin displayed as below format
    list_display=['question','option']

# setting Option model in django admin
@admin.register(Option)
class MCQAdmin(admin.ModelAdmin):
    
    # after data get saved field(s) in django admin displayed as below format
    list_display=['option1','option2','option3','option4']

# setting Question model in django admin
class QuestionAdmin(admin.ModelAdmin):
    
    # after data get saved field(s) in django admin displayed as below format
    list_display = ['question']
