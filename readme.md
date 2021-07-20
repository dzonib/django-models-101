## Migrations -> when work on models run them
`python manage.py make migrations`
go to database and create tables from models

`python manage.py migrate` goes through all migrations that have not been executed 
and applies them to database

`python manage.py shell` navigated in our project folder we get shall we can 
play with database

`from book_outlet.models import Book` - import book model

`harry_potter = Book(title="Harry potter 1 - the ps", rating=5)` instantiate new Book, you need to pass values for those 
fields as arguments

`harry_potter.save()` every class that extends model class has methods like save. Save
saves data to database (django make sql query and executes its for us)

example => `lord_of_the_rings = Book(title="Lord of the rings", rating=4)` then `lord_of_the_rings.save()`

`Book.objects.all()` django gives us object field, because we inherited models class. We have 
many methods on object field. One of them is `.all()` which gives us all QuerySet of all items

    def __str__(self):
        return f"{self.title} ({self.rating})
        
        Adding this as model method give us more readable view of model
        when using Book.objects.all()
                
