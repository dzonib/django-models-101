from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Author(models.Model):
    first_name: models.CharField(max_length=100)
    last_name: models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # author = models.CharField(null=True, max_length=100)

    # on_delete:
    #   models.CASCADE - if author is deleted, deleted all related books
    #   models.PROTECT - avoid deletion
    #   models.SET_NULL - sets author to null if deleted
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    is_bestselling = models.BooleanField(default=False)

    # db index, helps performance when making queries we use slug a lot
    # id field automatically has an index, others do not
    # problem is when creating index on its own decreases performance when ever you add new entry to db
    # make index fields you use a lot for querying
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    # Harry Potter 1 to harry-potter-1

    # blank has implications in admin site as well, it makes fields non required when entering data through admin panel
    # editable=False makes it disappear and non required, good if you have default entry, like for slug

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    # def save(self, *args, **kwargs):
    #
    #     slug_to_be = self.title + " " + str(self.id)
    #
    #     self.slug = slugify(slug_to_be)
    #
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"
