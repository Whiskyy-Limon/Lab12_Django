from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, ChoiceViewSet, CategoryViewSet, SeriesViewSet

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'series', SeriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
