from django.urls import path , include
from exam.views import ExamDetailCreateView, MCQCreateView, ExamDetailListView, SolutionCreateView, ExamScheduleCreateView,ExamScheduleListView,OptionCreateView,QuestionCreateView
from rest_framework.routers import DefaultRouter

app_name = 'exam'


router = DefaultRouter()
router.register('create-exam',ExamDetailCreateView,basename='create-exam')
router.register('que-list',ExamDetailListView,basename='que-list')
router.register('create-question',QuestionCreateView,basename='create-question')
router.register('create-option',OptionCreateView,basename='create-option')
router.register('create-mcq',MCQCreateView,basename='create-mcq')
router.register('add-solution',SolutionCreateView,basename='add-solution')
router.register('add-schedule',ExamScheduleCreateView,basename='add-schedule')
router.register('schedule-list',ExamScheduleListView,basename='schedule-list')


urlpatterns = [
    path('',include(router.urls)),
    # path('list/', ExamDetailListView.as_view()),
    # path('create-mcq/', MCQCreateView.as_view()),
    # path('add-solution/', SolutionCreateView.as_view()),
    # path("add-schedule/", ExamScheduleCreateView.as_view()),
]
