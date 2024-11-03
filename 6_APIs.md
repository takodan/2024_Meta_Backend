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
    6. `python manage.py makemigrations`
    7. `python manage.py migrate`

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



## Module 2 Django Rest Framework (DRF)
1. DRF is a toolkit for building Web APIs on top of Django.
2. DRF features
    1. Serialization and Deserialization
    2. Request and Response Handling
    3. API Viewer: to test HTTP methods
    4. ViewSet Classes: CRUD view sets
    5. Authentication
3. Installing DRF
    1. `pipenv install django`
    2. `pipenv shell`
    3. `django-admin startproject projectname .`
    4. `python manage.py startapp appname`
    5. `pipenv install djangorestframework`
    6. add DRF in settings.py
        ```py
            INSTALLED_APPS = [
                'rest_framework',
            ]
        ```
    7. use DRF in app
4. DRF api_view decorators
    1. Example: converts the django function view into an API view
    ```py
    # views.py
    from django.shortcuts import render
    from rest_framework.response import Response
    from rest_framework import status
    from rest_framework.decorators import api_view

    @api_view()
    def books(request):
        return Response('list of the books', status=status.HTTP_200_OK)
    ```
    2. Example: Defines allowed methods with decorators
    ```py
    @api_view(['GET', 'POST'])
    def books(request):
        if request.method == 'GET':
            return Response('List of books', status=status.HTTP_200_OK)
        elif request.method == 'POST':
            return Response('Book created', status=status.HTTP_201_CREATED)
    ```
5. Class-based views in DRF
    1. Example
    ```py
    # views.py
    from django.shortcuts import render
    from rest_framework.response import Response
    from rest_framework import status
    from rest_framework.view import APIview
    class BookList(APIView):
        def get(self, request):
            return Response({"message":'list of the books'}, status=status.HTTP_200_OK)
    ```
    ```py
    # urls.py at app level
    from . import views
    urlpatterns = [
        path('books', views.BookList.as_view())
    ]
    ```

6. DRF built-in class-based views: ViewSets
    1. ViewSets
    ```py
    # views.py
    from rest_framework import viewsets

    Class BookView(viewsets.ViewSet):
        def list(self, request):
        	return Response({"message":"All books"}, status.HTTP_200_OK)
        def create(self, request):
        	return Response({"message":"Creating a book"}, status.HTTP_201_CREATED)
        def update(self, request, pk=None):
        	return Response({"message":"Updating a book"}, status.HTTP_200_OK)
        def retrieve(self, request, pk=None):
        	return Response({"message":"Displaying a book"}, status.HTTP_200_OK)
        def partial_update(self, request, pk=None):
            return Response({"message":"Partially updating a book"}, status.HTTP_200_OK)
        def destroy(self, request, pk=None):
        	return Response({"message":"Deleting a book"}, status.HTTP_200_OK)
    ```

    2. ViewSets routing 
    ```py
    # urls.py at app level
    from . import views
    urlpatterns = [
        # access the `api/books` endpoint with GET and POST methods.
        path('books', views.BookView.as_view(
        	{
            	'get': 'list',
            	'post': 'create',
        	})
        ),
        # access the `api/books/{pk}` endpoint with GET, PUT, PATCH and DELETE methods.
        path('books/<int:pk>',views.BookView.as_view(
        	{
            	'get': 'retrieve',
            	'put': 'update',
            	'patch': 'partial_update',
            	'delete': 'destroy',
        	})
        )
    ]
    ```

    3. ViewSets routing with SimpleRouter class
    ```py
    from rest_framework.routers import SimpleRouter

    # `trailing_slash=False` for remove slash at the end of url
    router = SimpleRouter(trailing_slash=False)
    router.register('books', views.BookView, basename='books')
    urlpatterns = router.urls
    ```

    4. ViewSets routing with DefaultRouter class: It creates an API root endpoint (with a trailing slash).
    ```py
    from rest_framework.routers import DefaultRouter
    router = DefaultRouter(trailing_slash=False)
    router.register('books', views.BookView, basename='books')
    urlpatterns = router.urls
    # you can access the API root view by you visit `api/` endpoint
    ```

    5. ModelViewSet: include list, retrieve, create, update, and destroy (No need to define methods manually)
    ```py
    from rest_framework import viewsets
    from .models import Book
    from .serializers import BookSerializer

    class BookViewSet(viewsets.ModelViewSet):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
    ```
    6. ReadOnlyModelViewSet: only include list and retrieve (No need to define methods manually)
    ```py
    from rest_framework import viewsets
    from .models import Book
    from .serializers import BookSerializer

    class BookReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
    ```
7. DRF built-in class-based views: Generic views
    1. Generic views offer a particular functionality
    ```py
    from django.contrib.auth.models import User
    from myapp.serializers import UserSerializer
    from rest_framework import generics
    from rest_framework.permissions import IsAdminUser

    class BookList(generics.ListCreateAPIView):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        # all API calls must be authenticated
        permission_classes = [IsAdminUser]
    
    ```
    2. other generics class: https://www.django-rest-framework.org/api-guide/generic-views/#concrete-view-classes
    3. Selectively enable authentication
    ```py
    def get_permissions(self):
        permission_classes = []
        # anyone will be able to make GET call, but other HTTP methods will require authentication
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]
            return [permission() for permission in permission_classes]
    ```
    4. Return resources created by the authenticated users only
    ```py
    class BookView(generics.ListCreateAPIView):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        permission_classes = [IsAuthenticated]
        # override the get_queryset method
        def get_queryset(self):
            return Book.objects.all().filter(user=self.request.user)
    ```
    5. Override default behavior
    ```py
    class BookView(generics.ListCreateAPIView):
        queryset = Book.objects.all()
        serializer_class = BookSerializer  
        def get(self, request, *args, **kwargs):
            return Response(‘new response’)
    ```

        
8. Example: `booklist_api`
    1. create `booklist_api` app
    2. add `booklist_api` into settings.py
    3. add class in models.py
    4. do migrations
    5. add BookView and SingleBookView class in views.py
    6. create serializers.py at app level
    7. create urls.py at app level
    8. add path at project level



9. Django Debug Toolbar
    1. https://github.com/django-commons/django-debug-toolbar

10. Serializers
    1. Example: `serializer`
        1. add class in models.py
        2. do migrations
        3. create serializers.py
        4. add menu_item and single_item function in views.py

    2. Model serializers: Functions identically to the previous Serializers
        1. Example: `booklist_api`
            1. edit serializers.py at app level


11. relationship serializers
    1. Example: `booklist_api`
        1. edit models.py
            1. to create a link between the databases, you'll need to add data to the new one first.
            2. add Category class
            3. do migrations
            4. add category as a ForeignKey in Book class
            5. do migrations again
        2. edit serializers.py
            1. Method 1: create a related serializer
            2. Method 2: add depth
        3. if you use function views, you also need to edit views.py
        ```py
        # views.py
        @api_view()
        def menu_item(request):
            item = MenuItem.object.select_related("category").all()
            serialized_item = MenuItemSerializer(item, many=True)
            return Response(serialized_item.data)
        ```


12. Deserializers
    1. Example: `booklist_api`
        1. edit serializers.py
            1. add additional write_only variable for POST
        2. if you use function views, you also need to edit views.py
        ```py
        # views.py
        from rest_framework.response import Response
        from rest_framework.decorators import api_view
        from .models import MenuItem
        from .serializers import MenuItemSerializer
        from django.shortcuts import get_object_or_404
        from rest_framework import status

        @api_view(['GET','POST'])
        # return all menu item
        def menu_item(request):
            if request.method == 'GET':
                item = MenuItem.object.all()
                serialized_item = MenuItemSerializer(item, many=True)
                return Response(serialized_item.data)
            if request.method == 'POST':
                serialized_item = MenuItemSerializer(data=request.data)
                serialized_item.is_valid(raise_exception=True)
                serialized_item.validated_data
                serialized_item.save()
                return Response(serialized_item.data, status.HTTP_201_CREATED)

        # return menu item by id
        def single_item(request, id):
            # item = MenuItem.object.get(pk=id)
            item = get_object_or_404(MenuItem, pk=id)
            serialized_item = MenuItemSerializer(item)
            return Response(serialized_item.data)
        ```

13. Renderers
    1. Change the response renderer by adding/changing `Accept` header
        1. Example
        ```bash
        Accept: application/json
        Accept: text/html
        ```
    2. setting DRF Renderers
    ```py
    # settings.py
    # add
    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
        ]
    }
    ```
    3. other renderer
        1. `djangorestframework-xml`: `Accept: application/xml`
        2. `djangorestframework-csv`: `Accept: text/csv`
        3. `djangorestframework-yaml`: `Accept: application/yaml`
    ```bash
    pipenv install djangorestframework-xml
    pipenv install djangorestframework-csv
    pipenv install djangorestframework-yaml
    ```
    ```py
    # settings.py
    # add xml renderer
    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.BrowsableAPIRenderer',
            'rest_framework_xml.renderers.XMLRenderer',
            'rest_framework_csv.renderers.CSVRenderer', 
            'rest_framework_yaml.renderers.YAMLRenderer', 
        ]
    }
    ```
    4. TemplateHTMLRenderer and StaticHTMLRenderer Example
    ```py
    from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer
    from rest_framework.decorators import api_view, renderer_classes

    @api_view() 
    @renderer_classes ([TemplateHTMLRenderer])
    def menu(request):
        items = MenuItem.objects.select_related('category').all()
        serialized_item = MenuItemSerializer(items, many=True)
        return Response({'data':serialized_item.data}, template_name='menu-items.html')

    @api_view(['GET'])
    @renderer_classes([StaticHTMLRenderer])
    def welcome(request):
        data = '<html><body><h1>Welcome To Little Lemon API Project</h1></body></html>'
        return Response(data)
    ```
