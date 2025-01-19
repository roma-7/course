from .models import *
from modeltranslation.translator import TranslationOptions,register


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('text', 'question')


@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ('text', 'test')


@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('title',)
