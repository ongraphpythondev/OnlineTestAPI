from xml.dom import NotFoundErr
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.permissions import IsAuthenticatedExaminer, IsAuthenticatedExaminee

from rest_framework.viewsets import ViewSet , ModelViewSet
from accounts.models import CustomUser

from exam.models import Exam_Detail, MCQ, Option, Question, Solution, Exam_Schedule
from exam.serializers import SolutionSerializer, MCQSerializer, ExamDetailSerializer, ExamScheduleSerializer,OptionSerializer,QuestionSerializer


# Creating Exam
class ExamDetailCreateView(ModelViewSet):
    permission_classes = (IsAuthenticatedExaminer,)
    serializer_class = ExamDetailSerializer
    queryset = Exam_Detail.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['examiner'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# Showing Exam list
class ExamDetailListView(ViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ExamDetailSerializer

    # def get_queryset(self):
    #     me = self.request.GET.get('me')
    #     uid = self.request.GET.get('id')
    #     if me:
    #         Exam_Detail.objects.filter(examiner=self.request.user)
    #     elif uid:
    #         Exam_Detail.objects.filter(examiner__id=uid)
    #     else:
    #         return Exam_Detail.objects.all()
    
    def list(self,request):
        exam = Exam_Detail.objects.all()
        serializer = ExamDetailSerializer(exam , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

# Creating Question and Options
class MCQCreateView(ViewSet):
    permission_classes = (IsAuthenticatedExaminer,)
    serializer_class = MCQSerializer
    queryset = MCQ.objects.all()
    
    def create(self,request):
        serializer = MCQSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.error , status=status.HTTP_400_BAD_REQUEST)


class QuestionCreateView(ModelViewSet):
    permission_classes = (IsAuthenticatedExaminer,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()



class OptionCreateView(ModelViewSet):
    permission_classes = (IsAuthenticatedExaminer,)
    serializer_class = OptionSerializer
    queryset = Option.objects.all()
    

# Creating Solution for Existing Question in MCQ 
class SolutionCreateView(ModelViewSet):
    permission_classes = (IsAuthenticatedExaminer,)
    serializer_class = SolutionSerializer
    queryset = Solution.objects.all()
    
    
    

# Creating Test for time and Date for exam
class ExamScheduleCreateView(ModelViewSet):
    permission_classes = (IsAuthenticatedExaminer,)
    serializer_class = ExamScheduleSerializer
    queryset = Exam_Schedule.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class ExamScheduleListView(ViewSet):
    permission_classes = (IsAuthenticatedExaminee,)
    serializer_class = ExamScheduleSerializer
    
    def list(self,request):
        exam = Exam_Schedule.objects.all()
        serializer = ExamScheduleSerializer(exam , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

