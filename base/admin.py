from django.contrib import admin

from base.models import Language, Genra, Book, Author, Publisher


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['language']
    ordering = ['language']


admin.site.register(Language, LanguageAdmin)


class GenraAdmin(admin.ModelAdmin):
    list_display = ['genra']
    ordering = ['genra']


admin.site.register(Genra, GenraAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_on']
    ordering = ['created_on']


admin.site.register(Author, AuthorAdmin)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_on']
    ordering = ['created_on']


admin.site.register(Publisher, PublisherAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'edition', 'price', 'discount', 'author', 'publisher', 'number_of_pages', 'language',
                    'available', 'genra', 'published_date']
    ordering = ['created_on']


admin.site.register(Book, BookAdmin)
