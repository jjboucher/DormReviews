# DormReviews
![Screenshot](https://raw.githubusercontent.com/jjboucher/DormReviews/main/static/screenshot.png)

### Contributors:
* Joshua Boucher (team lead)
* Season Chowdhury
* Georges Elizee
* Andy Li

### Instructions:
0. If you do not have Python installed, install it from https://www.python.org/downloads/
1. Clone this repository: `git clone https://github.com/jjboucher/DormReviews` (or download as zip from the [GitHub repo site](https://github.com/jjboucher/DormReviews))
2. Run `pip install django`
3. Run `pip install Pillow`
4. Run `pip install django-test-without-migrations`
5. Change directory (cd) to the root DormReviews directory and run:<br />`python manage.py migrate`
6. Then run:<br />`python manage.py runserver`
7. Once the server is running, try out the app in your browser at http://localhost:8000/dormapp/.

### Project structure:
* **Models** are defined in `/dormapp/models.py`
* **Templates**, written in HTML with embedded Django tags, are located in `/dormapp/templates/`
  * All pages extend `base.html`, with contains the logo heading and stylesheet/script references
* **Views** functions are located in `/dormapp/views.py`
  * Most views call custom database queries, which are located in `/dormapp/helpers/queries.py`
* Test cases are in `/dormapp/tests.py`
* Database: `/db.sqlite3`
* Static files are located in `/static/`
* Media files are located in `/media/`
* Project settings: `/DormReviews/settings.py`
* Project URL configurations are defined in `DormReviews/urls.py` and app URLs are defined in `/dormapp/urls.py`
