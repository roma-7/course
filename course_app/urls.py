from .views import *
from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




router = routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'category', CategoryViewSet, basename='categories')
router.register(r'lesson', LessonViewSet, basename='lessons')
router.register(r'assignment', AssignmentViewSet, basename='assignments')
router.register(r'question', QuestionViewSet, basename='questions')
router.register(r'option', OptionViewSet, basename='options')
router.register(r'exam', ExamViewSet, basename='exams')
router.register(r'certificate', CertificateViewSet, basename='certificates')
router.register(r'cart', CartViewSet, basename='carts')
router.register(r'cart_item', CartItemViewSet, basename='cart_items')
router.register(r'course_review', CourseReviewViewSet, basename='course_reviews')
router.register(r'teacher', TeacherViewSet, basename='teachers')


urlpatterns = [
    path('', include(router.urls)),
    path('course/', CourseListAPIView.as_view(), name='course_list'),
    path('course/<int:pk>', CourseDetailAPIView.as_view(), name='course_detail'),
    path('courses/create/', CreateCourseAPIView.as_view(), name='create_course'),
    path('courses/<int:id>/update/', UpdateCourseAPIView.as_view(), name='update_course'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

