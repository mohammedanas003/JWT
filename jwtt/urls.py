from django.urls import path
from .views import RegistrationAPI
from rest_framework.routers import DefaultRouter
from .views import TeacherAPI

router=DefaultRouter()
router.register('teacher',TeacherAPI)




urlpatterns=router.urls+[
    path('register/',RegistrationAPI.as_view())
]