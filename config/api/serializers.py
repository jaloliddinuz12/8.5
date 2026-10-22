from rest_framework import serializers
from .models import Genre, Book, Comment

class BookSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price']

class GenreListSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ['id', 'name', 'books']

    def get_books(self, obj):
        kitoblar = obj.books.all()
        return [kitob.title for kitob in kitoblar]

class GenreDetailSerializer(serializers.ModelSerializer):
    books = BookSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ['id', 'name', 'books']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    genre_id = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        source='genre',
        write_only=True
    )
    genre = GenreSerializer(read_only=True)
    course = GenreSerializer(source='genre', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'price', 'genre', 'course', 'genre_id']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = ['id', 'book', 'user', 'text']
        read_only_fields = ['id', 'user']
