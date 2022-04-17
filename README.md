# DJANGO_APP

## How to Use ?

### Prerequisite
		1. Python 3.x
		2. Django
		3. Django-Rest

### Step 1. Clone and Install Packages
`git clone https://github.com/yashrajjain726/django-app`
`cd django-app`
`pip install -r requirements.txt`

### Step 2. Add your database settings
To add your database settings go to `djangoApp/djangoApp/settings.py`
and add your database setting in below scripts:
```
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.postgresql',  
		'NAME': '',  
		'USER': '',  
		'PASSWORD': '',  
		'HOST': '',  
		'PORT': '',  
		}
	}
```
### Step 3. Create Database Tables in your DB
To create your database tables, you need to run the following commands
`python manage.py makemigrations`
`python manage.py migrate`

### Step 4. Run the Server
To run the server, you need to run the command
`python manage.py runserver`

###  Urls in Server
1.  `/admin/` -> to view database along wiith its IAM role and authorization
2. `/product-api/` -> To get list of all data present in the product database and perform CRUD operation with it
4. `/operation-api/` -> To get list of all data present in the operation database and perform CRUD operation with it
6. `/operation-filter/` -> to get operation data between dates using `from_date` and `to_date` params



**Note**: `measurement_unit` takes choice between `['Kg', 'Liters', 'Units']` and `direction` takes choice between `['IN', 'OUT']`


