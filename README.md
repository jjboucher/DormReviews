# DormReviews

For software testers:
fork this repository, then cd into the parent DormReviews directory and run:

  python manage.py migrate

Then run:
 
  python manage.py runserver
  
You should be able to access the app by typing localhost:8000/dormapp/ in your browser.


# To run/create the database locally you can just run python manage.py migrate

# TO run the app on a localhost server:
# python manage.py runserver
# then go to localhost:8000/dormapp

# Use SQLite DBBrowser and you can browse the database.

# Reference this tutorial to play around with the database API:
# https://docs.djangoproject.com/en/4.1/intro/tutorial02/

#how to query based on id
https://django.fun/en/docs/django/4.0/topics/db/queries/#queries-over-related-objects

#static files and bootstrap tutorials:
https://data-flair.training/blogs/django-static-files-handling/
https://data-flair.training/blogs/django-bootstrap/#:~:text=In%20Django%20project%27s%20main%20settings,add%20boot%2F%20folder%20to%20STATIC_DIRS.&text=This%20will%20let%20Django%20search,can%20be%20loaded%20from%20there.
