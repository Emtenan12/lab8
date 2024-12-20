from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from .models import Book
from .models import Book_1,Author
from .models import Address, Student
from django.db.models import Count, Sum, Avg, Max, Min
from .forms import BookForm
from .forms import StudentForm, AddressForm



def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, 'bookmodule/index.html', {"name": name})

def index2(request, val1):
    try:
        val1 = int(val1)  # Try to convert val1 to an integer
        return HttpResponse(f"value1 = {val1}")
    except ValueError:
        return HttpResponse("error, expected val1 to be integer")


def viewbook(request, bookId):
    # Define two example books
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    
    # Initialize targetBook as None
    targetBook = None
    
    # Check if the bookId matches one of the books
    if book1['id'] == bookId:
        targetBook = book1
    elif book2['id'] == bookId:
        targetBook = book2
    
    # Prepare context with the found book
    context = {'book': targetBook}
    
    # Render the bookmodule/show.html template with the context
    return render(request, 'bookmodule/show.html', context)

def viewbook(request, bookId):
 # assume that we have the following books somewhere (e.g. database)
 book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
 book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
 targetBook = None
 if book1['id'] == bookId: targetBook = book1
 if book2['id'] == bookId: targetBook = book2
 context = {'book':targetBook} # book is the variable name accessible by the template
 return render(request, 'bookmodule/show.html', context)

#lab5p2
def link_page(request):
    return render(request, 'bookmodule/links.html')


def formatting_view(request):
    return render(request, 'bookmodule/formatting.html')

def listing_view(request):
    return render(request, 'bookmodule/listing.html')

def tables_view(request):
    return render(request, 'bookmodule/tables.html')

#lab4
def index(request): 
    return render(request, "bookmodule/index.html")

def list_books(request): 
    return render(request, 'bookmodule/list_books.html') 

def viewbook(request, bookId): 
    obj=Book.objects.all.get(id=bookId)
    return render(request, 'bookmodule/one_book.html',{'books.view_one_book':obj}) 

def aboutus(request): 
    return render(request, 'bookmodule/aboutus.html') 
#lab6
def search_books(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        filtered_books = []

        for book in books:
            contained = False
            if isTitle and keyword in book['title'].lower():
                contained = True
            if not contained and isAuthor and keyword in book['author'].lower():
                contained = True

            if contained:
                filtered_books.append(book)

        return render(request, 'bookmodule/bookList.html', {'books': filtered_books})

    return render(request, 'bookmodule/search.html')


def __getBooksList():
    return [
        {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'},
        {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'},
        {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    ]

def simple_query(request):
    mybooks =Book.objects.filter(title__icontains='Honorable')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def lookup_query(request):
    mybooks = Book.objects.filter(author__isnull=False) \
                           .filter(title__icontains='Honorable') \
                           .filter(edition__gte=2) \
                           .exclude(price__lte=100)[:10]  # Limit to 10 results

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
def task1(request):
    books = Book.objects.filter(Q(price__lte=100))
    return render(request, 'bookmodule/task1.html', {'books': books})

def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=2) & ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task3.html', {'books': books})

def task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})



def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    print("Stats fetched:", stats)  # Debugging output
    return render(request, 'bookmodule/task5.html', {'stats': stats})

def task7(request):
    city_counts = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task7.html', {'city_counts': city_counts})

#lab9

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        edition = request.POST.get('edition')
        obj= Book(title=title, author=author, price=price, edition=edition)
        obj.save()
        return redirect('books.view_one_book_lap9',bookId=obj.id)
    return render(request, 'bookmodule/add_book.html')


def view_one_book_lab9(request, bookId):
    obj=Book.objects.get(id=bookId)
    return render(request, 'bookmodule/one_BOOKlap9.html', {'book': obj})

def book_list_lab9(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/bookList_lab9.html', {'books': books})

def UpdateBookWithoutForms(request,id):
    obj = Book.objects.get(id=id)
    if request.method=="POST":
        titleval=request.POST.get('title')
        autherval=request.POST.get('author')
        priceval=request.POST.get('price')
        editionval=request.POST.get('edition')
        obj.title=titleval
        obj.author=autherval
        obj.price=priceval
        obj.edition=editionval
        obj.save()
        return redirect('books.view_one_book_lap9',bookId=obj.id)
    return render(request,"bookmodule/UpdateBook.html",{"obj":obj})

def DeleteBOOK(request,id):
    obj = Book.objects.get(id=id)
    if request.method=='POST':
        obj.delete()
        return redirect("books.book_list_lab9")
    return render(request,"bookmodule/deleteBook.html",{'obj':obj})

def add_book_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books.book_list_form')
    else:
        form = BookForm()
    return render(request, 'bookmodule/add_book_form.html', {'form': form})

# List all books
def book_list_form(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/book_list_form.html', {'books': books})

# Update an existing book
def update_book_form(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books.book_list_form')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/update_book_form.html', {'form': form})

# Delete a book
def delete_book_form(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('books.book_list_form')
    return render(request, 'bookmodule/delete_book_form.html', {'book': book})

#-------------practice------

def prac_home(request):
    books = Book_1.objects.all()
    return render(request, 'bookmodule/prac_home.html', {'books':books})


def prac_listbooks(request):
    books = Book_1.objects.all()
    return render(request, 'bookmodule/prac_listbooks.html', {'books': books})

def book_details(request, book_id):
    book = Book_1.objects.get(id=book_id)
    return render(request, 'bookmodule/book_details.html', {'book': book})

#lab 10
# List Students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Add Student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form, 'action': 'Add'})

# Update Student
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form, 'action': 'Update'})

# Delete Student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})

