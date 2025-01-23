import django_filters
from .models import Course
#
# class CourseFilter(django_filters.FilterSet):
#     class Meta:
#         model = Course
#         fields = ['price', 'level']

class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = {
            'level': ['exact'],
            'price': ['gt', 'lt']
        }