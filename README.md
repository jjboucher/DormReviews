# DormReviews

Instructions for software testers:

0. if you do not have Python installed, install Python from https://www.python.org/downloads/
1. clone this repository: `git clone https://github.com/jjboucher/DormReviews`

2. run `pip install django`
3. run `pip install Pillow`
4. run `pip install django-test-without-migrations`

5. change directory (cd) to the parent DormReviews directory and run:

  `python manage.py migrate`

6. Then run:
 
  `python manage.py runserver`
  
You should be able to access the app by typing `localhost:8000/dormapp/` in your browser.
