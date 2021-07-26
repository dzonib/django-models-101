## Migrations -> when work on models run them
`python manage.py makemigrations`
go to database and create tables from models

`python manage.py migrate` goes through all migrations that have not been executed 
and applies them to database

`python manage.py shell` navigated in our project folder we get shall we can 
play with database

Creating data.

`from book_outlet.models import Book` - import book model

`harry_potter = Book(title="Harry potter 1 - the ps", rating=5)` instantiate new Book, you need to pass values for those 
fields as arguments

`harry_potter.save()` every class that extends model class has methods like save. Save
saves data to database (django make sql query and executes its for us)

example => `lord_of_the_rings = Book(title="Lord of the rings", rating=4)` then `lord_of_the_rings.save()`

Or you can use .create() so you do not have ti instantiate new book.

`Book.objects.create(title="Harry Potter", rating=5)`

`Book.objects.all()` django gives us object field, because we inherited models class. We have 
many methods on object field. One of them is `.all()` which gives us all QuerySet of all items

    def __str__(self):
        return f"{self.title} ({self.rating})
        
        Adding this as model method give us more readable view of model
        when using Book.objects.all()
                
When adding fields to model that is already migrated to database, you need to specify that the data
dan be null with null=True argument

`    author = models.CharField(null=True, max_length=100)`

or you can add blank=True. That would allowed field to be empty in database, by default that is not the case.

Alternative to those two ways is adding default value

`is_bestselling = models.BooleanField(default=False)`

You can select data from queryset like this:

    >>> Book.objects.all()[1]
        <Book: Lord of the rings (4)>
    >>> Book.objects.all()[1].is_bestselling
        False
    >>> Book.objects.all()[1].rating
        4
        
Updating data.

`harry_potter = Book.objects.all()[0]`     

`harry_potter.author = "J.K. Rowling"`

`harry_potter.is_bestselling = True`

To update data in database we need to use save method.

`harry_potter.save()`

If .save() has been used on an object that has not been saved to database before, it will add new
item. If it is used on object that exists in database, it will update fields.

Deleting data.

`harry_potter.delete()`

Getting item from db.
Use id if you are getting only one item
`Book.objects.get(id=3)`

You can use other properties but its not recommended
`Book.objects.get(title="some title")`

If you want to get all entries with .filter().

`Book.objects.filter(is_bestselling=True)`

or multiple conditions

`Book.objects.filter(is_bestselling=True, rating=2)`

rating is smaller then 3, check django docs for filtering syntax, field lookup

`Book.objects.filter(rating__lt=3, title__contains="sometitle")`

or (we use pipe)

`from djang.db.models import Q`

`Book.objects.filter(Q(rating__lt3) | Q(is_bestselling=True))`

and (we use coma)

`from djang.db.models import Q`

`Book.objects.filter(Q(rating__lt3), Q(is_bestselling=True))`


Query set will only be executed when we use it, good for performance.

## Django admin

First create superuser
`python manage.py createsuperuser`

To make django aware that certain data should be managed through django admin
in app folder (book_outlet -> admin.py file), you need to register models for admin interface

`admin.site.register(Book)`