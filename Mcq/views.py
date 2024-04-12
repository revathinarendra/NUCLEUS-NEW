from django.views.generic.list import ListView
from .models import Question, Subject
from django.db.models import Q

from django.views.generic import DetailView
from .models import Subject, Topic, SubTopic
 
class SubjectListView(ListView):
    model = Subject
    template_name = 'mcq/subject.html'
    context_object_name = 'subjects'

class SearchResultsView(ListView):
    model = Subject
    template_name = 'mcq/search_result.html'  # Ensure you have this template
    # Your search logic here
    def get_queryset(self):
      query = self.request.GET.get('query')
      print("Query parameter:", query)
      object_list = Subject.objects.all()
      if query:
        object_list = object_list.filter(
            Q(subject_name__icontains=query)
        )
      print("Filtered queryset:", object_list)
      return object_list


class TopicListView(DetailView):
    model = Subject
    template_name = 'mcq/subjecttopic.html'
    context_object_name = 'subject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject = self.get_object()
        context['topics'] = Topic.objects.filter(subject_name=subject)
        return context

class SubTopicListView(DetailView):
    model = Topic
    template_name = 'mcq/subjecttopic.html'
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = self.get_object()
        context['subtopics'] = SubTopic.objects.filter(topic_name=topic)
        return context

class QuestionListView(ListView):
    model = Question
    template_name = 'mcq/question.html'
    context_object_name = 'questions'

    def get_queryset(self,**kwargs):
        sub_topic_name = self.kwargs.get('sub_topic_name')
        if sub_topic_name:
            #context = super().get_context_data(**kwargs)
            #Question = self.get_object()
            #context['Question'] = Question.objects.filter(sub_topic_name=sub_topic_name)
            #return context
            return Question.objects.filter(sub_topic_name=sub_topic_name)
        else:
            return Question.objects.none()  # or handle if no subtopic is selected
