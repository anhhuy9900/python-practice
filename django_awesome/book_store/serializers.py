from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Book, Author, Reporter


class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = ('name', 'email')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name')


class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    rating = serializers.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    content = serializers.CharField(max_length=1000, default=None)
    author = AuthorSerializer(allow_null=True, default=None)
    reporter = ReporterSerializer(allow_null=True, default=None)

    class Meta:
        model = Book
        fields = ('__all__')
