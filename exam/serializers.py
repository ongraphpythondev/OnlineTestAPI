from optparse import Option
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from exam.models import Exam_Detail, MCQ, Solution, Exam_Schedule,Option,Question


class MCQSerializer(ModelSerializer):

    # def validate_question(self, value):
    #     if value not in MCQ.objects.filter(examiner=self.context.get('request')):
    #         raise serializers.ValidationError("Can Only Add options to own exam's questions")
    #     return value

    class Meta:
        model = MCQ
        fields = ['examer','question','option']
        
class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['question']


class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = ['option1','option2','option3','option4']


class SolutionSerializer(ModelSerializer):

    # def validate_exam(self, value):
    #     if value not in self.context.get('request').user.exam.all():
    #         raise serializers.ValidationError("Please create exam because you Can Only Add questions to own exams")
    #     return value

    class Meta:
        model = Solution
        fields = '__all__'


class ExamDetailSerializer(ModelSerializer):
    class Meta:
        model = Exam_Detail
        fields = '__all__'


class ExamScheduleSerializer(ModelSerializer):
    class Meta:
        model = Exam_Schedule
        fields = '__all__'
