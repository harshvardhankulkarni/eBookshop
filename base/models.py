from django.db import models


class Language(models.Model):
    language = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.language}'


class Genra(models.Model):
    genra = models.CharField(null=False, max_length=255, unique=True)

    def __str__(self):
        return f'{self.genra}'


class Author(models.Model):
    name = models.CharField(null=False, max_length=255)
    about = models.TextField(null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Publisher(models.Model):
    name = models.CharField(null=False, max_length=255)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    title = models.CharField(null=False, max_length=255)
    edition = models.IntegerField(max_length=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='bookImages', null=True, blank=True)
    price = models.DecimalField(decimal_places=2, null=False, max_digits=5)
    discount = models.IntegerField(max_length=2, default=10)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, blank=True)
    number_of_pages = models.BigIntegerField(null=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    available = models.BooleanField(null=False, default=True)
    genra = models.ForeignKey(Genra, on_delete=models.CASCADE)
    published_date = models.DateField()
    # TODO: add ISBN number field
    # ISBN_number = models.UUIDField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
