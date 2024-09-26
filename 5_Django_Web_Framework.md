# Django Web Framework
## Module 1 Introduction to Django
1. Django was first created for a newspaper publisher web application.
2. Django is commonly used for
    1. ML and AI
    2. Scalable web apps
    3. SaaS apps: such as cloud-storage app
    4. OTT platforms
3. Django Web application structure
    1. Project: represents the entire web application
    2. App: an independent, reusable sub-module of a project
4. Create a Django project
    1. create project directory
    2. create virtual environment
```bash
    python3 -m venv venv_name
    source venv_name/bin/activate
```
    3. create Django project
```bash
    django-admin startproject project_name project_dir
```
    4. run development project, default address http://127.0.0.1:8000/
```bash
    python3 manage.py runserver
```
5. Django project files
    1. `__init__.py`: for a folder to be recognized by Python as a package.
    2. `manage.py`: command line utility. local version of django-admin that points to local setting.py
    3. `settings.py`: Django configures specific parameters.
    4. `urls.py`: contains a list of object `urlpatterns`, used by the servers routing the application to the mapped view.
    5. `asgi.py`: used by the servers following the ASGI standard to serve asynchronous web applications.
    6. `wsgi.py`: entry point for such WSGI-compatible servers to serve your classical web application.
6. `settings.py`
    1. `INSTALLED_APPS`
        1. a list of strings.
        2. represents the path of an app.
    2. `DATABASES`
        1. a dictionary. Use SQLite by default.
        2. specifies the configuration of databases to be used by the application.
    3. `DEBUG = True`
        1. debug mode. True by default.
    4. `ALLOWED HOSTS`
        1. a list of strings. Empty by default.
        2. qualified host/domain
    5. `ROOT_URLCONF`.
        1. point to the urls.py module in which the project's URL patterns are found.
    6. `STATIC_URL`
        1. points to the folder where the static files are placed.

7. Create a Django app
```bash
    python manage.py startapp app_name app_dir
```
8. Django app files
    1. `views.py`
        1. user-defined functions
        2. is called when client's request URL matches a URL pattern defined in project's urls.py file
    

9. add urls in urls.py
    1. directly inside project's urls.py
```py
    from app_dir import views
    urlpatterns = [
        path('url_path/', views.function_name, name = function_name)
    ]
```
