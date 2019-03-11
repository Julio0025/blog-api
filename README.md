# blog-api
This is a django-rest blog api that has user post create/remove/update/delete methods, user session authentication, logout and single post content soundex filter.

## To get started you will need
###
* python 3.6
* django 1.11.*
###

# To get things running
Clone the repository

```commandline
git clone https://github.com/Julio0025/blog-api.git
```

Create virtual environment (optional but highly advisable)

```commandline
cd blog_api
virtualenv --python=python3 venv

```
activate venv 1) windows 2) linux/unix
```commandline
venv\scripts\activate
source venv/bin/activate
```

install required pip packages

```commandline
pip install -r requirement_list.txt
```

run server

```commandline
cd blog_api
python manage.py runserver
```

# API Usage
Browsable api is enabled go to url 
```commandline
/api/post/
```
To use soundex filtering navigate to. ID 
```commandline
/api/post/{ID}/{KEYWORD}/
```

To run tests
```commandline
python manage.py test
```




