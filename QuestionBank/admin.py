from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Bookmark, BookmarkQuestion, SolvedQuestions, UnsolvedQuestions

# Register your models here.

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date_added')
    search_fields = ('user__username',)

@admin.register(BookmarkQuestion)
class BookmarkQuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'bookmark', 'created_at', 'updated_at')
    search_fields = ('user__username', 'question__question')
    list_filter = ('created_at', 'updated_at')

@admin.register(SolvedQuestions)
class SolvedQuestionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'solved_question', 'selected_option', 'is_correct', 'last_answered')
    search_fields = ('user__username', 'solved_question__question')
    list_filter = ('is_correct', 'last_answered')

@admin.register(UnsolvedQuestions)
class UnsolvedQuestionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'unsolved_question', 'timestamp')
    search_fields = ('user__username', 'unsolved_question__question')
    list_filter = ('timestamp',)
