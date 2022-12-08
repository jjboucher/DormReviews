# DormReviews
![Screenshot](/static/screenshot.png)

### Contributors:
* Joshua Boucher (team lead)
* Season Chowdhury
* Georges Elizee
* Andy Li

### Instructions:
0. if you do not have Python installed, install it from https://www.python.org/downloads/
1. clone this repository: `git clone https://github.com/jjboucher/DormReviews` (or download as zip from GitHub repo site)
2. run `pip install django`
3. run `pip install Pillow`
4. run `pip install django-test-without-migrations`
5. change directory (cd) to the root DormReviews directory and run:<br />`python manage.py migrate`
6. Then run:<br />`python manage.py runserver`
7. Once the server is running, try out the app in your browser at http://localhost:8000/dormapp/.

### Project structure:
* **Models** are defined in `/dormapp/models.py`
* **Templates**, written in HTML with embedded Django tags, are located in `/dormapp/templates/`
  * All pages extend `base.html`, with contains the logo heading and stylesheet/script references
* **Views** functions are located in `/dormapp/views.py`
  * Most views call custom database queries, which are located in `/dormapp/helpers/queries.py`
* Test casese are in `/dormapp/tests.py`
* Database: `/db.sqlite3`
* Static files are located in `/static/`
* Media files are located in `/media/`
* Project settings: `/DormReviews/settings.py`
* Project URL configurations are defined in `DormReviews/urls.py` and app URLs are defined in `/dormapp/urls.py`
