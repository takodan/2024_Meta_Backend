# Application Programming Interface (API)
## Module 1 Introduction to API
1. review of HTTP
    1. https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
    2. HTTP methods
        1. GET
        2. POST: create
        3. PUT: update
        4. PATCH: partially update
        5. DELETE
    3. HTTP request makeup
        1. https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages#http_requests
        2. HTTP method
        3. URL: the request target
        4. HTTP version
        5. Headers
            1. user-agent
            2. accept: desired response format
            3. cookies
            4. referrers
        6. Body
    4. HTTP response makeup
        1. https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages#http_responses
        2. HTTP version
        3. Response status code
            1. https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
            2. 100: informational
            3. 200: successful
            4. 300: redirection
            5. 400: client error
            6. 500: server error
        4. Response status text
        5. headers
        6. Body

2. RESTful characteristics
    1. client-server architecture
    2. stateless
    3. cacheable: responses can be saved
    4. layered: system can be split into layers
    5. uniform interface

3. Naming conventions for APIs
    1. lowercase
    2. hyphens in between words
    3. camel case variable with curly brace
    4. Avoid verbs, use nouns
    5. Avoid special characters
    5. Avoid file extensions, user query parameters for data type
    6. no trailing slash (slash at the end)

4. tools for API development
    1. Curl: HTTP calls from command line
    2. httpie: HTTP calls from command line
    2. Postman: test and debug
    3. Insomnia: store, organize, and execute REST API request
    4. httpbin: HTTP Request and Response service
    5. Mockaroo: fake data generator service
    6. Mockapi: create mock API endpoints

5. Create a Django project using pipenv
     1. `pipenv install {django}`
     2. `pipenv shall`
     3. `django-admin startproject {projectname} {.}`
     4. `python manage.py startapp {appname}`
     5. `python manage.py runserver {port}`

6. REST best practices
    1. KISS (Keep it simple stupid)
        1.  Avoid overloading a single API with multiple tasks.
        2. Each API should perform one specific job well.
    2. Filtering, Ordering, and Pagination
        1. Provide options to filter, order, and paginate results for better user experience.
    3. Versioning
        1. Implement versioning to prevent breaking client applications with changes.
        2. Maintain up to two versions of any resource to manage complexity and reduce errors.
    4. Caching
        1. Cache API responses to reduce database load.
    5. Rate Limiting and Monitoring
        1. Use rate limiting to prevent API abuse by restricting the number of requests over a time period.
    6. Monitor metrics like latency, status codes (errors), and network bandwidth to ensure performance and identify potential issues.

7. API Security
    1. Secure Socket Layer (SSL )
        1. Using SSL certificates ensures APIs are served over HTTPS, not HTTP.
    2. Signed URLs
        1. Signed URLs limit access to specific resources temporarily.
        2. Hash-based Message Authentication Code (HMAC) is commonly used to create these signatures.
    3. Token-based Authentication
        1. Users receive a token after logging in, and this token is then used in each API call for secure access
        2. Preferred over basic authentication
        3. JSON Web Token (JWT): A widely-used standard
    4. Cross-Origin Resource Sharing (CORS) Policy
        1. Controls which domains can make requests to the API
    5. Firewalls

8. Access control
    1. Roles and Privileges
        1. Roles are collections of privileges that define what users can do in the system
    2. Authorization vs. Authentication
        1. Authentication: verifies identity
        2. Authorization: grants or restricts access to specific actions after authentication
    3. Design Approaches for Role Management
        1. Single Comprehensive Role: Create a role with all necessary privileges for users needing multi-role access.
        2. Multiple Roles per User
            1. Assign specific roles to users who require access to multiple domains.
            2. it's easy to adjust privileges as needed.

9. Organizing an API project
    1. Splitting into Multiple Apps
        1. Divide a large app into smaller
        2. Focused apps to ensure manageability and productivity, particularly with Django.
    2. Use of Virtual Environments
    3. Use versioning
        1. Create separate versions rather than updating the old app
        2. Avoid breaking existing apps
    4. Dependency Management
        1. Save dependencies and their versions in a requirements.txt file (`pip freeze > requirements.txt`).
        2. Use a Pipfile.lock with pipenv.
    5. Organize Resource Folders
        1. Maintain separate resource folders for each app to avoid conflicts
    6. Split Settings Files
        1. Use separate settings files instead of a single, lengthy settings file for easier management and editability.
        2. Use tools like Django Split Settings to manage this structure.
    7. Business Logic in Models:
        1. Place business logic in models rather than views to keep code organized, reusable, and manageable.

10. Book List API project: GET and POST
    1. The project is a simple API to manage books in a bookstore
    2. Steps
        1. create a Django model: 
            1. Book with fields: title, author, and price.
            2. index price.
            ```py
            class Book(models.Model):
                title = models.CharField(max_length=255)
                author = models.CharField(max_length=255)
                price = models.DecimalField(max_digits=5, decimal_places=2)

                class Meta:
                    indexes = [
                        models.Index(fields=['price']),
                    ]
            ```
        2. add Book to admin.py
            ```py
            from .models import Book

            admin.site.register(Book)
            ```
        3. perform migrations
            ```bash
            python manage.py makemigrations
            python manage.py migrate
            ```
        4. add books into database
            1. create superuser
                ```bash
                python manage.py createsuperuser
                ```
            2. run the server
                ```py
                python manage.py runserver
                ```
            3. go to admin page to add books
        5. create a URL in app level
            ```py
            # app/urls.py

            from django.urls import path
            from . import views

            urlpatterns = [
                path('books',views.books),
            ]
            ```
        6. add app url to project url
            ```py
            # project/urls.py
            from django.contrib import admin
            from django.urls import path, include

            urlpatterns = [
                path('admin/', admin.site.urls),
                path('api/', include('BookListAPI.urls')), 
            ]
            ```
        7. create views for api
            ```py
            # app/views.py
            from django.db import IntegrityError
            from django.http import HttpResponse, JsonResponse
            from .models import Book
            from django.views.decorators.csrf import csrf_exempt
            from django.forms.models import model_to_dict

            @csrf_exempt
            def books(request):
                if request.method == 'GET':
                    books = Book.objects.all().values()
                    return JsonResponse({"books":list(books)})
                elif request.method == 'POST':
                    title = request.POST.get('title')
                    author = request.POST.get('author')
                    price = request.POST.get('price')
                    book = Book(
                        title = title,
                        author = author,
                        price = price
                    )
                    try:
                        book.save()
                    except IntegrityError:
                        return JsonResponse({'error':'true','message':'required field missing'},status=400)

                    # Convert model instances to JSON using model_to_dict
                    return JsonResponse(model_to_dict(book), status=201)
            ```
        8. update settings.py
        ```py
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'app',
        ]
        ```