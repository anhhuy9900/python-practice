from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render
from .models import Book, Author, Reporter


# Create your views here.


def index(request):
    return HttpResponse("Index Page")


def get_all(request):
    all_objects = Book.objects.all()
    print(all_objects)
    return HttpResponse(all_objects)


def create(request):
    b = Book(title="test")
    b.save()
    return HttpResponse("Create book success")


def update(request):
    b = Book.objects.filter(title="test")
    print(b)
    values = {
        "title": "test new",
        "rating": 4,
        "content": "Content new"
    }
    b.update()
    obj = Book(**values)
    obj.save()
    return HttpResponse("Create book success")


# One to one relationship
def create_author_relation(request):
    # author = Author.objects.get(first_name="Huy")
    author = Author(first_name="Hoang", last_name="Nguyen")
    author.save()
    b = Book(title="test 3", rating="3", content="test 3333", author=author)
    b.save()
    return HttpResponse("Create book relation author success")


def get_authors(request):
    all_objects = Author.objects.all()
    print(all_objects)
    return HttpResponse(all_objects)


def create_author(request):
    a = Author(first_name="Huy", last_name="Nguyen")
    a.save()
    return HttpResponse("Create author success")


def create_reporter(request):
    a = Reporter(name="Huy Reporter", email="reporter@email.com")
    a.save()
    return HttpResponse("Create report success")


# One to one Reporter relationship
def create_reporter_relation(request):
    # author = Author.objects.get(first_name="Huy")
    reporter = Reporter.objects.get(email="reporter@email.com")
    b = Book(title="test 31", rating="3", content="test", reporter=reporter)
    b.save()
    return HttpResponse("Create book relation reporter success")
