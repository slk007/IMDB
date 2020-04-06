from django.urls import path

from .views import MovieDetailView, MovieListView,MovieCategory, MovieLanguage, MovieSearch, MovieYear

app_name = 'movies'

urlpatterns = [
    path('', MovieListView.as_view(), name='list'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='detail'),
    path('category/<str:category>/', MovieCategory.as_view(), name='category'),
    path('language/<str:language>/', MovieLanguage.as_view(), name='language'),
    path('year/<int:year>', MovieYear.as_view(), name='year'),
    path('search/', MovieSearch.as_view(), name='search'),
]
