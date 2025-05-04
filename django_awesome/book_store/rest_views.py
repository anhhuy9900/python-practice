from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer
from .models import Book


class BookViewDetail(APIView):
    def get(self, request, *args, **kwargs):
        if id:
            book = Book.objects.get(id=kwargs.get('pk'))
            serializer = BookSerializer(book)
        else:
            return Response({"status": "success", "data": None}, status=status.HTTP_404_NOT_FOUND)

        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        try:
            item = get_object_or_404(Book, id=kwargs.get('pk'))
            item.delete()
        except:
            return Response({"status": "success", "data": None}, status=status.HTTP_404_NOT_FOUND)
        return Response({"status": "success", "data": "Item Deleted"})

    def put(self, request, *args, **kwargs):
        book = Book.objects.get(id=kwargs.get('pk'))
        print(book)
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            # serializer.save()
            # book = Book(**serializer.data)
            # book.update(**request.data)
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


class BookView(APIView):
    # List
    @action(
        methods=['get'],
        detail=True,
    )
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    # Create
    @action(
        methods=['post'],
        detail=True,
    )
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = Book(**request.data)
            book.save(force_insert=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)