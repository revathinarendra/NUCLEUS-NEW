from django.urls import path
from .views import QuestionListView, SearchResultsView, SubTopicListView, SubjectListView, TopicListView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_view_name'),
    path('subjects/', SubjectListView.as_view(), name='subject-list'),
    path('start_course/<int:pk>/', TopicListView.as_view(), name='start_course'),
    path('start_course/subtopics/<int:pk>/', SubTopicListView.as_view(), name='start_course_subtopic'),
    path('subtopic/<int:pk>/questions/', QuestionListView.as_view(), name='subtopic_questions'),
]