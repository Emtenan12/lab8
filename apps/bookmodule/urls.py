from django.urls import path
from . import views  # Import views from the current directory


urlpatterns = [
    path('', views.index),
    path('index2/', views.index2),  # This will handle the case when val1 is missing
    path('index2/<int:val1>/', views.index2),  # This will handle the case when val1 is present
    path('<int:bookId>', views.viewbook),
    #lab 5 p2
    path('html5/links/', views.link_page, name='link_page'),
    path('html5/text/formatting', views.formatting_view, name='formatting'),
    path('html5/listing', views.listing_view, name='listing'),
    path('html5/tables', views.tables_view, name='tables'),
    path('', views.index, name= "books.index"), 
    #lab4
    path('list_books/', views.list_books, name= "books.list_books"), 
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"), 
    path('aboutus/', views.aboutus, name="books.aboutus"), 
    #lab 6
    path('search/', views.search_books, name='search_books'),
    path('simple/query', views.simple_query, name='simple_query'),
    path('lookup/query', views.lookup_query, name='lookup_query'),
    #lab8
    path('lab8/task1', views.task1, name='task1'),
    path('lab8/task2', views.task2, name='task2'),
    path('lab8/task3', views.task3, name='task3'),
    path('lab8/task4', views.task4, name='task4'),
    path('lab8/task5', views.task5, name='task5'),
    path('lab8/task7', views.task7, name='task7'),
   #lab9
    path('oneBOOK/<int:bookId>', views.view_one_book_lab9, name="books.view_one_book_lap9"),
    path('lab9_part1/addbook', views.add_book, name='add_book'),
    path('lab9_part1/editbook/<id>', views.UpdateBookWithoutForms, name='updateBook'),
    path('book_list_lab9', views.book_list_lab9, name="books.book_list_lab9"),
    path('lab9_part1/deletebook/<id>', views.DeleteBOOK, name='DeleteBOOK'),

    path('lab9_part2/add/', views.add_book_form, name='add_book_form'),
    path('lab9_part2/list/', views.book_list_form, name='books.book_list_form'),
    path('lab9_part2/edit/<int:id>/', views.update_book_form, name='update_book_form'),
    path('lab9_part2/delete/<int:id>/', views.delete_book_form, name='delete_book_form'),

    #lab 10
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('students/edit/<int:id>/', views.update_student, name='update_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),


    #prac
    path('prac/home', views.prac_home, name='prac_home'),
    path('prac/listbooks', views.prac_listbooks, name='prac_listbooks'),
    path('prac/book_details/<int:book_id>/', views.book_details, name='book_details'),

]

