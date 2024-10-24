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
    1. Update `settings.py` after created an app
    ```py
    INSTALLED_APPS = [ 
    'django.contrib.admin', 
    'django.contrib.auth',  
    'django.contrib.contenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles',
 
    'app_name.apps.MyappConfig', 
    ] 
    ```


8. Django app files
    1. `views.py`
        1. user-defined functions
        ```py
        from django.shortcuts import render

        # Create your views here.
        from django.http import HttpsResponse

        def fun_name(request):
            return HttpsResponse("Hello World!")
        ```
        2. is called when client's request URL matches a URL pattern defined in project's urls.py file
    2. `models.py`
        1. The data models required for processing in this app are created in this file.
    3. `tests.py`
        1. The tests to be run on the app.
    

9. add urls in urls.py
    1. create a `urls.py` in app folder then import it to project
    ```py
        # in app
        from django.urls import path 
        from . import views
        urlpatterns = [
            path('url_path/', views.function_name, name = "function_name")
        ]
    ```
    ```py
        # in project
        from django.contrib import admin 
        from django.urls import include, path 

        urlpatterns = [ 
            path('admin/', admin.site.urls),
            path('url_path/', include('app.urls')), 
        ] 
    ```

    2. directly inside project's `urls.py`
    ```py
        # in project
        from django.contrib import admin 
        from django.urls import include, path
        
        from app import views

        urlpatterns = [
            path('admin/', admin.site.urls), 
            path('url_path/', views.function_name, name = "function_name"), 
        ] 
    ```

10. Three-tier architecture
    1. Presentation tier: user interface
    2. Application tier: web and application server
    3. Data tier: database server

11. Django's Model, View and Template (MVT) architecture
    1. Model-View-Controller (MVC) architecture
        1. The controller intercepts the client requests
        2. The controller coordinates with the view and model layers to send the appropriate response back to the client
        3. The model is responsible for data definitions, processing logic and interaction with the backend database.
        4. The view is the presentation layer of the application.
    2. MVT architecture
        1. Django's URL dispatcher mechanism is equivalent to the controller in the MVC architecture. (`urls.py`)
        2. The model is the data layer of the application (`models.py`)
            1. A model is a Python class.
            2. Django perform CRUD operations in an object-oriented way instead of invoking SQL queries.
            3. The models perform CRUD operations with the data from a view function
        2. The view is the layer that undertakes the processing logic. (`view.py`)
            1. The view function reads the path, query, and body parameters.
            2. A view can be a user-defined function or a class.
        3. The template is the presentation layer.
            1. A template contains a mix of static HTML and Django Template Language code blocks.
            2. You place Template web pages in the templates folder
            3. Django uses any context data from the view inserted in these blocks to formulate a dynamic response.

12. Django MVT Example
    1. `urls.py`
    ```py
    from . import views
    urlpatterns = [
        path("menu/<int:menu_id>", views.menu_by_id, name="menu_by_id" ),
    ]
    ```

    2. `views.py`
    ```py
    from .models import Menu
        def menu_by_id(request, menu_id):
            # with models.py
            menu = Menu.object.get(pk=menu_id)

            # with 
            return render(request, "menu_card.html", {"menu":menu})
    ```

    3. `menu_card.html`
    ```html
    <body style="background-color: #EDEFEE;">
        <h2> Items: {{menu.menu_item}}</h2>
        <h3> Cuisine: {{menu.cuisine}}</h3>
    
    </body>
    ```


## Module 2 views
1. Views: take a request and return a response
```py
from django.http import HttpResponse

# function doesn't matter to django
def home(request):
    content = "<html><body><h1>Hello World</h1></body></html>"
    return HttpResponse(content)
```
2. Routing: The view function needs to be mapped to a URL in `urls.py`
    1. best practice
    ```py
        # urls.py in app
        from django.urls import path 
        from . import views
        urlpatterns = [
            path('url_path/', views.function_name, name = "function_name")
        ]
    ```
    ```py
        # urls.py in project
        from django.contrib import admin 
        from django.urls import include, path 

        urlpatterns = [ 
            path('admin/', admin.site.urls),
            path('url_path/', include('app.urls')), 
        ] 
    ```
3. Function based views
```py
def view_name(request):  

      if request.method=='GET':  
            #perform read or delete operation on the model  

      if request.method=='POST':  
            #perform insert or update operation on the model  
            context={ } #dict containing data to be sent to the client  

      return render(request, 'mytemplate.html', context) 
```
4. Class based views
```py
from django.views import View 
class MyView(View): 
    def get(self, request): 
        # logic to process GET request
        return HttpResponse('response to GET request') 
 
    def post(self, request): 
        # <logic to process POST request> 
        return HttpResponse('response to POST request') 
```
5. `django.views.generic` module contains several generic view classes that provide the functionality required to perform certain tasks.
6. HTTP
    - https://developer.mozilla.org/en-US/docs/Web/HTTP
    1. request
        - https://developer.mozilla.org/en-US/docs/Web/HTTP/Session#example_requests
        ```
        GET / HTTP/1.1
        Host: developer.mozilla.org
        Accept-Language: fr
        ```
        1. request method
            1. GET: retrieve
            2. POST: send
            3. PUT: update
            4. DELETE: remove
        2. request header
        - https://developer.mozilla.org/en-US/docs/Glossary/HTTP_header
    2. response
        - https://developer.mozilla.org/en-US/docs/Web/HTTP/Session#example_responses
        ```
        HTTP/1.1 200 OK
        Content-Type: text/html; charset=utf-8
        ```
        1. status code
        - https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

7. request in Django view
    - https://docs.djangoproject.com/en/5.1/ref/request-response/
    1. `request.method`: HTTP methods
    ```py
    if request.method == 'GET': 
        do_something() 
    elif request.method == 'POST': 
        do_something_else_if()
    ```
    2. `request.GET` and `request.POST`: A dictionary-like object containing all given method parameters
    3. `request.COOKIES`: A dictionary containing all cookies.
    4. `request.FILES`: A dictionary-like object containing all uploaded files.
    5. `request.user`: An object of django.contrib.auth.models.User class.
    ```py
    if request.user.is_authenticated(): 
        # Do something for logged-in users. 
    else: 
        # Do something for anonymous users. 
    ```
    6. `request.has_key()`: It check whether the GET or POST parameter dictionary has a value for the given key.

8. response in Django view
```py
from django.http import HttpResponse 
from django.template import loader 
def index(request): 
    template = loader.get_template('app_name/index.html') 
    context={}  
    return HttpResponse(template.render(context, request))
```

9. URLs
    - https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_URL#basics_anatomy_of_a_url
    1. `https://www.example.com.uk/home/2024/summer/`
    2. Scheme: protocol `https://`
    3. Subdomain: `www`
    4. Second-level domain: `example`
    5. Top-level domain: category and country `com` `uk`
    6. File path: `home
    7. URL parameters: `2024` `summer`
    8. Query strings: `?year=2024&menu=summer`

10. parameters in Django
    1. Path parameter example: `http://127.0.0.1:8000/request_info/menu/pizza/30`
    ```py
    def menu(request, item, price):
        content = f"Item: {item} Price: {price}"
        return HttpResponse(content, content_type='text/html', charset='utf-8')
    ```
    ```py
    # urls.py in app.
    urlpatterns = [
        path('', views.request_info, name = "request_info"),
        path('menu/<item>/<price>', views.menu, name = "menu")
    ]
    ```
    ```py
    # urls.py in project.
    urlpatterns = [
        path('', include('practice_http.urls')),
    ]
    ```
    2. path converter: Django parses the received value to the string type by default.
    ```py
    # urls.py in app.
    urlpatterns = [
        path('menu/<str:item>/<int:price>', views.menu, name = "menu")
    ]
    ```
    - https://docs.djangoproject.com/en/5.1/topics/http/urls/#path-converters
    3. Query parameter example: `http://127.0.0.1:8000/request_info/qryMenu/?item=egg&price=100`
    ```py
    def qry_menu(request): 
        item = request.GET['item'] 
        price = request.GET['price']
        content = f"Item: {item} Price: {price}"
        return HttpResponse(content, content_type='text/html', charset='utf-8') 
    ```
    ```py
    # urls.py in app.
    urlpatterns = [
        path('', views.request_info, name = "request_info"),
        path('qryMenu/', views.qryMenu, name = "qryMenu"),
    ]
    ```
    ```py
    # urls.py in project.
    urlpatterns = [
        path('', include('practice_http.urls')),
    ]
    ```
    4. Body parameters example:
        1. create a template `form.html`
        ```html
        <form action="/getform/" method="POST"> 
            {% csrf_token %} 
            <p>Name: <input type="text" name="id"></p> 
            <p>UserID :<input type="name" name="name"></p> 
            <input type="submit"> 
        </form> 
        ```
        2. modify `views.py`
        ```py
        def showform(request): 
            return render(request, "form.html") 

        def getform(request): 
            if request.method == "POST": 
                id=request.POST['id'] 
                name=request.POST['name'] 
            return HttpResponse("Name:{} UserID:{}".format(name, id)) 
        ```
        3. modify `urls.py` at app level
        ```py
        urlpatterns = [
            path('showform/', views.showform, name = "showform"),
            path("getform/", views.getform, name='getform'),
        ]
        ```
        4. The form data that the user posts becomes part of the request body.
        5. The view function passes these body parameters from the request.POST dictionary-like attribute.

11. Regular expressions in URLs
    1. RegEx cheat sheet
    - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions/Cheatsheet
    2. Example
    ```py
    from django.urls import path, re_path
    from . import views
    urlpatterns = [
        path("menu_item/10", views.display_menu)
        path(r"^menu_item/([0-9]{2})/$", views.dispaly_menu_)
    ]
    ```

12. Error handling
    - https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    1. common error code
        1. 400 Bad Request
        2. 403 Forbidden:
        3. 404 Not Found
        4. 500 Internal Server Error
    2. customize the look of these views

13. URL Namespacing
    1. A namespace is needed if the view function of the same name is defined in more than one app
    2. The application namespace is created by defining app_name variable in the application's urls.py.
    ```py
    #demoapp/urls.py
    from django.urls import path  
    from . import views    
    app_name='demoapp' 
    urlpatterns = [  
        path('', views.index, name='index'),      
    ] 
    ```
    ```py
    #newapp/urls.py 
    from django.urls import path 
    from . import views 
    app_name='newapp' 
    urlpatterns = [ 
        path('', views.index, name='index'), 
    ] 
    ```
    3. The Instance namespace is used the `namespace` parameter in the `include()` function.
    ```py
    #in demoproject/urls.py 
    urlpatterns=[ 
        # ... 
        path('demo/', include('demoapp.urls', namespace='demoapp')), 
        # ... 
    ]
    ```
    4.  url tag and namespace
        1. Use the url tag to obtain the URL path dynamically
        ```html
        <form action="{% url 'login' %}" method="POST"> 
            {% csrf_token %} 
            <p>UserID: <input type="text" name="id"></p> 
            <input type="submit"> 
        </form>
        ```
        2. use namespace to find the specific view in the app
        ```html
        <form action="{% url 'demoapp:login' %}" method="post"> 
            {% csrf_token %} 
            <p>UserID: <input type="text" name="id"></p> 
            <input type="submit"> 
        </form> 
        ```

14. Class based views (again)
```py
from django.views import View 
class MyView(View): 
    def get(self, request): 
        # logic to process GET request
        return HttpResponse('response to GET request') 
 
    def post(self, request): 
        # <logic to process POST request> 
        return HttpResponse('response to POST request') 
```

</br>

## Module 3 Models
### Models & Migrations
1. Models Example
    1. in SQL
    ```sql
    CREATE TABLE user(
        "id" serial NOT NULL PRIMARY KEY,
        "first_name" varchar(30) NOT NULL,
        "last_name" varchar(30) NOT NULL
    );
    ```
    2. in Django models
    ```py
    from django.db import models
    class User(models.Model):
        # no need to define primary key
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
    ```
2. CURD in Django
    1. in SQL
    ```sql
    INSERT INTO user(id, first_name, last_name)
    VALUES (1, "John", "JJones");

    SELECT * FORM user WHERE id = 1;

    UPDATE user
    SET last_name = "Smith"
    WHERE id = 1;

    DELETE FROM user WHERE id = 1;
    ```
    2. in Django models
    ```py
    new_user= User(id=1, "John", "Jones")
    new_user.save()

    user = USER.objects.get(id=1)

    user = USER.objects.get(id=1)
    user.last_name = "Smith"
    user.save()

    User.objects.filer(id=1).delete()
    ```

3. Creating models
    1. add models object in "models.py" under the app
    2. add the app into the project "settings.py"
    ```py
    INSTALLED_APPS = [
    'app_name.apps.app_nameConfig'
    ]
    ```
    3. create the migrations script and apply the migrations
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
    4. then you can access the table through models
    5. you can also create custom function in models class

4. Migrations
    1. django implements models to the database schema
    2. `makemigrations`: Creates new migration files based on the changes made to the models in your Django app.
    3. `migrate`: Applies the migrations to the database, syncing the database schema with the current state of your models.
    ```bash
    # preview the migration operations without actually applying them
    python manage.py migrate --plan
    # revert the database schema to the specific migration
    python manage.py migrate app_name 0001
    ```
    4. `sqlmigrate` :Displays the SQL statements that will be run for a specific migration.
    5. `showmigrations`: Lists all migrations and their current status (whether they've been applied or not).

5. Registering models
    1. make models available in the Django admin interface
    2. admin.py file in the app
    ```py
    from django.contrib import admin
    from .models import Model_name

    admin.site.register(Model_name)
    ```

6. Foreign Keys in Django Example
    1. on_delete:
        1. CASCADE: deletes the object containing the ForeignKey
        2. PROTECT: Prevent deletion of the referenced object.
        3. RESTRICT: Prevent deletion of the referenced object by raising RestrictedError
```py
class DrinksCategory(models.Model):
    category_name = models.CharField(max_length = 200)

class Drinks(models.Model):
    drink = models.CharField(max_length = 100)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete = models.PROTECT, default = None relate_name = ")
```

7. Object Relationship Mapping (ORM)
    1. Django use ORM to interact with SQL
    2. you can also use Model.object to interact with SQL
    - https://docs.djangoproject.com/en/4.1/topics/db/queries/#retrieving-objects

</br>

### Models & Form
1. Form 
    1. Form class Example
    ```py
    from django import form
    class NameForm(form.Form):
        yourName = forms.CharField(label="Your name", max_length=100)
    ```
    2. Form fields
        1. CharField
        ```py
        name = forms.CharField(widget=forms.Textarea(attrs={"rows":5}))
        ```
        2. EmailField
        ```py
        email = forms.EmailField(label="Enter email address")
        ```
        3. DateField
        ```py
        date = forms.DateField(widget=NumberInput(attrs={"type":"date"}))
        ```
        4. ChoiceField
        ```py
        iterable_name = (
            ("a", "AAA"),
            ("B", "BBB"),
        )

        choice = forms.ChoiceField(widget=forms.RadioSelect,choices=iterable_name)
        ```
        5. IntegerField
        ```py
        num = forms.IntegerField(min_value=20, max_value=60)
        ```
        6. MultipleChoiceField
        7. FileField
        ```py
        upload = forms.FileField(upload_to ='uploads/')
        ```
        8. ImageField
    3. common fields argument
        1. required: True by default
        2. label
        3. initial: initial value
        4. help_text
    
2. ModelForm Example
    1. create a model in models.py
    ```py
    # Create your models here.
    class Booking(models.Model):
        first_name = models.CharField(max_length = 200)
        last_name = models.CharField(max_length = 200) 
        guest_count = models.IntegerField()
        reservation_time = models.DateField(auto_now=True)
        comments = models.CharField(max_length = 1000)

        # return first_name instead of object name
        def __self__(self):
            return self.first_name
    ```
    2. register the model in admin.py
    ```py
    # Register your models here.
    from .models import Booking

    admin.site.register(Booking)
    ```
    3. create the forms.py in the myapp directory 
    4. create a form in forms.py
    ```py
    from django import forms
    from .models import Booking

    class BookingForm(forms.ModelForm):
        class Meta:
            model = Booking
            field = "__all__"
    ```
    5. create the templates directory
    6. create the template name booking.html
    ```html
    <p> Booking for Little Lemon ! </p>

    <form action = "" method = "post", style="background-color: #E0E0E2;">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Submit">
    </form>
    ```
    6. create a view in views.py
    ```py
    from app_name.forms import BookingForm

    def form_view(request):
        form = BookingForm()
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()
        context = {"form" : form}
        return render(request, "booking.html", context)
    ```
    7. create url in urls.py
    ```py
    from . import views
    urlpatterns = [
        path('booking/', views.form_view),
    ]
    ```
    8. add AppNameConfig into project settings.py
    ```py
    INSTALLED_APPS = [
        'app_name.apps.AppNameConfig',
    ]
    ```
    9. do the migrations
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Admin
    1. Create a superuser 
        1. `python manage.py createsuperuser`
        2. enter username, email and password
        3. User creation can be performed through either the admin page or the command shell interface. 
    2. The admin page allows you to manage users, permissions, and databases.
    3. Django user classifications
        1. superuser
        2. staff user: can access the admin interface, but no operations are allowed by default.
        3. user: can't access the admin interface

### Database options
1. Setting up a MySQL
    1. install MySQL
    2. enter MySQL `mysql -u root -p`
    3. create a database for the project `Create database mydatabase;`
    4. create a MySQL user for the project 
    5. exit MySQL  `exit`
    6. install database client for python `pip3 install mysqlclient`
    7. enable MySQL in django project setting.py
    - https://docs.djangoproject.com/en/5.1/ref/settings/#databases
    8. run migrations
        ```bash
            python3 manage.py makemigrations
            python3 manage.py migrate
        ```

## Module 4 Template
1. use template in django
    1. create a HTML template
    2. create a view with template in views.py
    - `return render(request, 'template_path.html', {"key":"value_for_template"})`
    3. update urls.py
    4. update settings.py
        1. add app into `INSTALLED_APPS` list
        1. add template directory path into `TEMPLATES` list
2. create a template
    1. in views.py
    - `return render(request, 'template_path.html', {"key":"value_for_template"})`
    2. in HTML, `{{key}}` will be replace after rendering
    - `{{key}}` > `value_for_template`
    3. to add file (like an image)
        1. add a list call `STATICFILES_DIRS`
        2. add static file directory path into the list
        3. add `{% load static %}`at the beginning of the HTML
        4. add <img src="{% static 'img/dessert.jpg' %}">

3. Django Template Language components
    - https://docs.djangoproject.com/en/5.1/ref/templates/language/
    1. Variable: `{{ variable }}`
    2. Filters: for modify variables, e.g.,`{{ name|lower }}`
    3. Tags: `{% tag %}`, e.g., `{% if expression %}` `{% else %}` `{% endif %}`; `{% for i in iterable %}` `{% endfor %}`
    4. Comments: `{# comments #}`

4. Template inheritance
    1. include: it insert another template within the current template
    ```html
    <!-- navbar.html -->
    <nav>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about/">About</a></li>
        <li><a href="/contact/">Contact</a></li>
    </ul>
    </nav>
    ```
    ```html
    <!-- base.html -->
    <html>
    <head>
        <title>My Website</title>
    </head>
    <body>
        <!-- Include the navigation bar -->
        {% include 'navbar.html' %}
        
        <div>
            {% block block_name %}
            <!-- Content will go here -->
            {% endblock %}
        </div>
    </body>
    </html>
    ```
    2. extends: it inherits the base template's structure and can customize blocks content.
    ```html
    <!-- home.html -->
    <!-- extends from base.html -->
    {% extends 'base.html' %}

    <!-- add content in block -->
    {% block block_name %}
        <h1>Welcome to My Website</h1>
        <p>This is the homepage content.</p>
    {% endblock %}
    ```




