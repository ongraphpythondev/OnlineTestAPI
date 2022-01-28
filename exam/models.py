from django.db import models
from accounts.models import CustomUser
# Create your models here.

# Creating Exam_Detail model to store exam related exam related details
class Exam_Detail(models.Model):
    examiner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    info = models.TextField()
    duration = models.DurationField(help_text="hr:min:sec = 00:00:00")

    def __str__(self):
        return self.name

# Option to be shown in exam/test
class Option(models.Model):
    option1 = models.CharField(max_length=15)
    option2 = models.CharField(max_length=15)
    option3 = models.CharField(max_length=15)
    option4 = models.CharField(max_length=15)
    
    def __str__(self):
        return f'{self.option1},{self.option2},{self.option3},{self.option4}'
    
# Questions to be shown in exam/test
class Question(models.Model):
    question = models.TextField()
    def __str__(self) :
        return self.question
    
# MCQ model integrate use of data from Question and Option models
class MCQ(models.Model):
    examer = models.ForeignKey(Exam_Detail, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE , related_name='MCQ_Question')
    option = models.ForeignKey(Option, on_delete=models.CASCADE,related_name='MCQ_Option')
    
    def __str__(self) :
        return f"(Question : {self.question} , Option : {self.option})"

# Solution of Question(s) in Question model
class Solution(models.Model):
    exam = models.ForeignKey(Exam_Detail, on_delete=models.CASCADE)
    question = models.ForeignKey(
        MCQ, on_delete=models.CASCADE)
    answer = models.CharField(max_length=15)

    def __str__(self):
        return self.answer

# Time and date data on which exam/test will be held on.
class Exam_Schedule(models.Model):
    exam = models.ForeignKey(Exam_Detail, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True)
