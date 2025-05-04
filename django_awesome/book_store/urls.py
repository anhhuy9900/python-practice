from django.urls import path

from . import views
from .rest_views import BookViewDetail, BookView

urlpatterns = [
    path("", views.index),
    path("all", views.get_all),
    path("create", views.create),
    path("update", views.update),
    path("create-author", views.create_author),
    path("authors", views.get_authors),
    path("create-book-author", views.create_author_relation),
    path("create-reporter", views.create_reporter),
    path("create-book-reporter", views.create_reporter_relation),

    path("rest/<int:pk>", BookViewDetail.as_view()),
    path("rest", BookView.as_view()),
]