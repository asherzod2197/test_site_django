from django.contrib import admin
from .models import Category, Quiz, Question, UserResult


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    fields = ('order_index', 'question_md', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option')


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'question_count', 'created_at')
    list_filter = ('category', 'difficulty')
    search_fields = ('title', 'description')
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'quiz', 'correct_option', 'order_index')
    list_filter = ('quiz',)


@admin.register(UserResult)
class UserResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'total', 'percentage', 'duration_display', 'completed_at')
    list_filter = ('quiz', 'quiz__category')
    search_fields = ('user__username', 'quiz__title')
    readonly_fields = ('user', 'quiz', 'score', 'total', 'started_at', 'completed_at')
