# APIs

## Course Summary

- tools and resources to create and use APIs
- how APIs are used in the real-world
- REST API: key characteristics, benefits, states, and resource types, API requests to life cycle, principles of authentication and differences with authorization
- create routes with the correct naming conventions
- organize an API project
-
- install and set up Django Rest framework, or DRF.
- Use function and class based views to create API endpoints
- Convert and validate data, including map user input to database models using deserialization, use throttling and caching to optimize and protect your API
-
- Control access to your APIs and put systems in place to ensure you maintain their health
- Tools: insomnia

## Installation & configurations

### python virtual environment

### Django Project

### DRF[^APIs-wk2-m1-v2]

[^APIs-wk2-m1-v2]: [APIs wk2 video - Installing and setting up DRF](https://www.coursera.org/learn/apis/lecture/EE4hl/installing-and-setting-up-drf)

Use pipenv (to set up a new django project using pipenv instead of pip)

**Installation**

- in Terminal, go to project's folder and install django by running `pipenv install django`
- activate shell to work with `pipenv shell`
- create a new project and app. `django-admin startproject Booklist .` and `python3 manage.py startapp BookListAPI`
- install DRF `pipenv install djangorestframework`

**Configuration**

- open `settings.py` in project folder and add the DRF `rest_framework` and the new app `BookListAPI` to the end of `INSTALLED_APPS`.

**Create an API endpoint**

- in the `BookListAPI` folder open the `view.py` file, add the code for the default GET method and also add for the POST method
- map the method to an API endpoint by creating a `url.py` file in the folder
- include the App mapping into project mapping `url.py` file

- Run the server `python3 manage.py runserver` to use and test

## Notes

### REST API

REST API constraints

- client-server
- stateless
- cacheable
- layered
- uniform interface (URI / endpoint / URL)
- optional code on demand

Name conventions

- lowercase & hyphens
- forward slash
- use Nouns to indicate the resources dealing with
- {variables} in camelCase
- APIs can return xml or json format, but no file name extension; specify in query in endpoints
- endpoints end without forward slash at the end

Tools

- Curl
- Postman
- Insomnia REST client

API development

- Best practices
  - KISS
  - filter, order and pagination
  - Versioning (2)
  - Caching
- Security and authentication
  - SSL
  - HTTPS
  - Signed URLs
    - HMAC
  - Token-based Authentication
    - Json web token
    - ad hoc backend service
  - CORS
  - Firewalls
- Access control and authorization
  - roles and priviledges

Organize an API project

- Split. split into multiple de-coupled apps (prevent one big app, plan, smaller aims, multiple apps)
- Env. Avoid global env due to conflicts and issues
  - pipenv to isolate virtual env
- Version. upgrades might break; versioning, keep the old version, timely launch
- Save. save dependencies and versions (in a separate txt file)
  - `pip3 freeze > requirements.txt`
  - or pipenv automatic
- Foler. separate resource folder for each app
- Settings. split settings for each app, use Django split setting
- Models. Place logic in related models

Debug & mock

- Debug python is vscode: breakpoint, watch, network calls
- Django debug toolbar to debug APIs
- Mock APIs: imitate, test & develop
  - mock data generator & endpoints

### DRF

- Install & configuration
- Accept different request methods

Create APIs:

### DRF Routing[^DRFroutings]

- Regular routes
  - map a function from a `views.py` file to an API endpoint in the `urls.py` file. (And iclude in django.urls module)
- Routing to a class method
  - declare method as `@staticmethod` then map it.
- Routing class-based views
  - class extends `APIView` with HTTP verb-specific methods
  - Mapp the class in the `urls.py` file as a view: `path('books/<int:pk>', views.BookView.as_view())`
- Routing classes that extend viewsets
  - class extends `viewsets.ViewSet`, map `as_view()` with mapping of HTTP verbs/methods to class-defined functions
- Routing with `SimpleRouter / DefaultRouter` class
  - import and initiate a `SimpleRouter / DefaultRouter` object (with arg set for best naming convention: no trailing slash!)
  - register the ampping in `router.register` then `urlpatterns = router.urls`
  - can access both `api/books` and `api/books/1` as in the previous example!

[^DRFroutings]: [DRF routings](https://www.coursera.org/learn/apis/supplement/cFRCv/different-types-of-routing-in-drf)

### DRF View

Generic views VS ViewSets

- `from rest_framework import viewsets`

### DRF serializer

Translating query sets and model data into other Python and web-based data formats.

Serializers (model -> display)

- `items = MenuItem.objects.all(); serialized_item = MenuItemSerializer(items, many=True)`
- used to hide/format data to show (instead of showing querySet: `MenuItem.objects.all()` in the view)
- create a serializers file and create a class to extend `serializers.Serializer`
- pass the querySet into the serializer and display the serialized data
- map in the urls.py file `views.func_name`
- use `django.shortcuts -> get_object_or_404` to get specific item and display 404 page if not found, instead of crash error

Model serializers

- `class Meta: model... fields...`
- extends `serializers.ModelSerializer`, define `model` and `fields` to display
- rename a field: create a new field in the class and use `source='xxx'` to link to the old field, ex `stock = serializers.IntegerField(source="inventory")`
- calculated field

```py
from rest_framework import serializers
from .models import MenuItem
from decimal import Decimal

class MenuItemSerializer(serializers.ModelSerializer):
  stock = serializers.IntegerField(source="inventory")
  price_after_tax = serializers.SerializerMethodField(method_name="calculate_tax")
  class Meta:
    model = MenuItem
    fields = ['id', 'title', 'price', 'stock', 'price_after_tax']

  def calculate_tax(self, product:MenuItem):
    return product.price * Decimal(1.1)

# By setting the model attribute to MenuItem, it indicates that this serializer is associated with the MenuItem model.

# The Meta class can also be used to specify other metadata, such as the fields that should be serialized, the order in which they should appear, and any additional validation or formatting options.

# In the provided code, the Meta class specifies that the MenuItemSerializer should serialize the id, title, price, inventory, and price_after_tax fields of the MenuItem model. It also specifies that the inventory field of the model should be mapped to a stock field in the serialized output.

# Note that Meta is not required for a serializer class, but it can be used to customize its behavior and specify additional information about the associated model.

# the calculate_tax method receives the MenuItem instance that is being serialized.
```

Relationship serializers

- ex: a Category model that's related to the MenuItem model and show the Category title.
- when converting a connected model to string, also load the related model in a single SQL call instead of a separate query for better efficiency
- like this `items = MenuItem.objects.select_related('category').all()`
- add a separate serializer for Catogery and link to the MenuItemSerializer by calling it `category = CategorySerializer()`
  - can set access limit `read_only=True`
  - ex, create an id field with write access `category_id = serializers.IntegerField(write_only=True)`
- or set `depth = 1` for the Meta class

Display related model fields field as a hyperlink

- HyperlinkedRelatedField
  1. a view to map the URL pattern and name with `-detail` convention
  2. set the category field as `serializers.HyperlinkedrelatedField(queryset = Category.objects.all(), view_name='category-detail')` instead of `CategorySerializer()`
     - since the view follows convention, `view_name='...'` can be removed
  3. add context to the menu_items: `serialized_item = MenuItemSerializer(items, many=True, context={'request': request})` to display category field as a hyperlink in the menu-items endpoint.
- HyperlinkedModelSerializer
  1. follow same naming convention with `-detail`
  2. change the serializer class to extend `HyperlinkedModelSerializer`, no need to call `CategorySerializer()`!

Deserialization

- in the view method, add logic for the `POST` request to serialize
- check validity (can access `serialized_item.validated_data`) and save to database
- return reponse with status code.

```py
def menu_items(request):
  if request.method == 'GET':
    items = queryset
    serialized_item = serializer...
    return Response(serialized_item.data)
  if request.method == 'POST':
    serialized_item = MenuItemSerializer(data=request.data)
    serialized_item.is_valid(raise_exception=True)
    serialized_item.save()
    return Response(serialized_item.data, status.HTTP_201_CREATED)
```

### DRF renderer

- in diff format, application/json, XML, text/html, YAML, etc
- https://www.coursera.org/learn/apis/supplement/57qRB/different-types-of-renderers

### Filter, Order, Pagination

Filter

- ???

Order

- descending, ascending, multiple ordering

Pagination

- query parameters and code setup

### Caching

### Validation and sanitation

Access control

- set roles and priviledges

Authentication

- Djoser library

Signed URL & token ??

API throttling

- 2 classes
