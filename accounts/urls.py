from django.urls import path , include
from accounts.views import RegisterAPIView , LoginAPIView , LogoutAPIView
from rest_framework.routers import DefaultRouter

# setting routers of APIs for easy access
router = DefaultRouter()
# register API route
router.register('register',RegisterAPIView,basename='register')
# login API route
router.register('login',LoginAPIView,basename='login')
# logout API route
router.register('logout',LogoutAPIView,basename='logout')

urlpatterns = [
    path('',include(router.urls)),
]
