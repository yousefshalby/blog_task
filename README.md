# blog-task

## To install 

git clone https://github.com/yousefshalby/blog_task.git 

# create env 
  - python3 -m venv env

# install requirements
  - pip install -r requiremnts.txt

# create .env
  - SECRET_KEY=

# run project 
  - python3 manage.py makemigrations
  - python3 manage.py migrate
  - python3 manage.py runserver

# endpoints are:
  - signup: /api/signup
  - login: /api/login
  - log-out: /api/logout
  - create post: /api/posts
