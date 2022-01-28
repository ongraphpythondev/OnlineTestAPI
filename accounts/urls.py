from xml.etree.ElementInclude import include
from django.urls import path , include
from accounts.views import RegisterAPIView , LoginAPIView , LogoutAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('register',RegisterAPIView,basename='register')
router.register('login',LoginAPIView,basename='login')
router.register('logout',LogoutAPIView,basename='logout')

urlpatterns = [
    path('',include(router.urls)),
    # path('login/',LoginAPIView.as_view()),
]
