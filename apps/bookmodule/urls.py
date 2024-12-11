from django.urls import path
from . import views  # Import views from the current directory


urlpatterns = [
    path('', views.index),
    path('index2/', views.index2),  # This will handle the case when val1 is missing
    path('index2/<int:val1>/', views.index2),  # This will handle the case when val1 is present
    path('<int:bookId>', views.viewbook),
    path('html5/links/', views.link_page, name='link_page'),
    path('html5/text/formatting', views.formatting_view, name='formatting'),
    path('html5/listing', views.listing_view, name='listing'),
    path('html5/tables', views.tables_view, name='tables'),
    path('', views.index, name= "books.index"), 
    path('list_books/', views.list_books, name= "books.list_books"), 
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"), 
    path('aboutus/', views.aboutus, name="books.aboutus"), 
    path('search/', views.search_books, name='search_books'),
    path('simple/query', views.simple_query, name='simple_query'),
    path('lookup/query', views.lookup_query, name='lookup_query'),
    path('lab8/task1', views.task1, name='task1'),
    path('lab8/task2', views.task2, name='task2'),
    path('lab8/task3', views.task3, name='task3'),
    path('lab8/task4', views.task4, name='task4'),
    path('lab8/task5', views.task5, name='task5'),
    path('lab8/task7', views.task7, name='task7'),

]

