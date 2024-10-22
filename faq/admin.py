from django.contrib import admin
from .models import Question, Answer

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1  # Number of extra forms to display

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'created_at', 'has_answer')
    search_fields = ('question',)
    list_filter = ('created_at',)
    inlines = [AnswerInline]

    fieldsets = (
        (None, {
            'fields': ('question',)
        }),
    )
    ordering = ('id',)

    def has_answer(self, obj):
        return hasattr(obj, 'answer')
    has_answer.boolean = True
    has_answer.short_description = 'Has Answer'

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_question', 'answer', 'created_at')
    search_fields = ('answer', 'question__question')
    list_filter = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('question', 'answer')
        }),
    )
    ordering = ('id',)

    def get_question(self, obj):
        return obj.question.question
    get_question.short_description = 'Question'