from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
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


def link_page(request):
    return render(request, 'bookmodule/links.html')


def formatting_view(request):
    return render(request, 'bookmodule/formatting.html')

def listing_view(request):
    return render(request, 'bookmodule/listing.html')

def tables_view(request):
    return render(request, 'bookmodule/tables.html')


def index(request): 
    return render(request, "bookmodule/index.html")

def list_books(request): 
    return render(request, 'bookmodule/list_books.html') 

def viewbook(request, bookId): 
    return render(request, 'bookmodule/one_book.html') 

def aboutus(request): 
    return render(request, 'bookmodule/aboutus.html') 
    
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
