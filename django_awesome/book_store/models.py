from django.db import models
from django.core import validators
from django.core.validators import MinValueValidator, MaxValueValidator


# One to Many relationship with Book
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"first_name={self.first_name}, last_name={self.last_name}"


# One to One Relationship with Book
class Reporter(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.name, self.email)


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    content = models.CharField(max_length=1000, default=None)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    reporter = models.OneToOneField(Reporter, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"" \
               f"(title={self.title}), " \
               f"(rating={self.rating}), " \
               f"(content={self.content}), " \
               f"author=({self.author}), " \
               f"reporter=({self.reporter})"
