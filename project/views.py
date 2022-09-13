from django.shortcuts import render
from django.views.generic import ListView
from .models import Project, Search
from django.db.models import Q # new
# Create your views here.


class  ProjectListView(ListView):
  model = Project
  template_name = "project/project_list.html"
  context_object_name = 'project_list'


class SearchResultsListView(ListView):
  model = Project
  template_name = "project/search_results.html"
  context_object_name = "project_list"
  # queryset = Book.objects.filter(title__icontains='django')

  def get_queryset(self): # new
    query = self.request.GET.get('q')
    if self.request.user:
      search = Search(name = query, author = self.request.user)
      search.save()
    return Project.objects.filter(
      Q(name__icontains=query) |  Q(district__icontains=query) |  Q(price__icontains=query)
    )

  

