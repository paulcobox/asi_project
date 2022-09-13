from django.urls import path, include
from .views import ProjectListView, SearchResultsListView

urlpatterns = [
  path('', ProjectListView.as_view(), name="project_list"),
  path('search/', SearchResultsListView.as_view(), name='search_results'),
  ]