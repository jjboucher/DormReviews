# DormReviews

Instructions for software testers:

0. if you do not have Python installed, install it from https://www.python.org/downloads/
1. clone this repository: `git clone https://github.com/jjboucher/DormReviews` (or download as zip from GitHub repo site)

2. run `pip install django`
3. run `pip install Pillow`
4. run `pip install django-test-without-migrations`

5. change directory (cd) to the root DormReviews directory and run:<br />`python manage.py migrate`

6. Then run:<br />`python manage.py runserver`
  
Once the server is running, try out the app in your browser at https://localhost:8000/dormapp/.
