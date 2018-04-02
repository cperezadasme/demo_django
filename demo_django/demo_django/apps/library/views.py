from django.http import HttpResponse

from .models import Author, Book


def index(request):
    link_author = '<h2><a href= "author"> Autores </a></h2>'
    link_book = '<h2><a href= "book"> Libros </a></h2>'
    html = link_author + link_book
    return HttpResponse(html)


def author(request):
    authors = Author.objects.all().order_by('last_name')
    html = '<h1><b> Autores </b></h1>'
    for author in authors:
        name = author.name + ' ' + author.last_name
        html += '<h2>' + name + '</h2>'

    return HttpResponse(html)


def book(request):
    books = Book.objects.all().order_by('-publish_year')
    html = '<h1><b> Libros </b></h1>'
    for book in books:
        html += '<h2>' + book.name + '</h2>'
        html += '<h3>' + book.author.name + ' ' + book.author.last_name + '</h3>'
        html += '<h3> Año de publicacion: ' + book.publish_year + '</h3>'
        html += '<h3> Categoria: ' + book.category + '</h3>'

    return HttpResponse(html)
