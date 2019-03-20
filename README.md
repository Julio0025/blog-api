# blog-api
This is a django-rest api blog. It has user post CRUD and soundex post content search. 

## To get started you will need
###
* python 3.6
* django 1.11.*
###

# Getting started

1) Clone the repository

	```commandline
	git clone https://github.com/Julio0025/blog-api.git
	```

2) Create a virtual environment (optional but highly advisable)

	```commandline
	cd blog_api
	virtualenv --python=python3 venv
	```

3) Activate the virtual environment

	a) windows 
	```commandline
	venv\scripts\activate
	```

	b) linux/unix
	```commandline 
	source venv/bin/activate
	```

4) Install the required pip packages

	```commandline
	pip install -r requirement_list.txt
	```

5) Run the Django development server

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
	```
	/api/post/{ID}/{KEYWORD}/
	```

To run tests
	```
	python manage.py test
	```




