from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return ('Autor: ' + self.name + self.last_name)


class Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    publish_year = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
