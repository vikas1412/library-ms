from django.db import models
from django.urls import reverse
import uuid

class Genre(models.Model):
    """Model representing a book genre"""
    name = models.CharField(max_length=200, help_text="Enter a book genre")

    def __str__(self):
        return self.name

class Language(models.Model):
    """Modal representing language; ie, English, French, etc. Book language variable uses it."""
    name = models.CharField(max_length=200, help_text="Enter book language in which it is written.")

    def __str__(self):
        """String to represent language rather than object name in Admin page"""
        return self.name


class Book(models.Model):
    """Model representing a book. But not specifically a copy of book"""
    title = models.CharField(max_length=300, help_text="Enter book title")

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text="Enter brief summary of the book")

    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text="13 Character <a href='https://www.isbn-international.org/content/what-isbn'>ISBN number</a>")

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing modal object"""
        return self.title

    def get_absolute_url(self):
        """Return the url to access detail record for this object"""
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """Create a string for genre as Admin cannot support ManyToMany in 'list_display'"""
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'


class BookInstance(models.Model):
    """Modal representing a specific copy of a book; (that can be borrowed from the library if available"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this copy of book across whole library")
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book Availability')

    class Meta:
        """Ordering of BorrowInstance objects"""
        ordering = ['due_back']

    def __str__(self):
        """String representation for Modal obejct."""
        return f"{self.id} ({self.book.title})"

    def book_status(self):
        return str(self.status)

    def due_date_status(self):
        return str(self.due_back)


class Author(models.Model):
    """Modal representing the author of the book"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Date of death', null=True, blank=True)

    class Meta:
        """Ordering of Author modal instance"""
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns url to access particular author object."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String object representation"""
        return f"{self.last_name} {self.first_name}"

