# Blog TestTask

### Challenge
Object of this task is to create a simple REST API. You have to use Django and Django rest
framework.

**Blog**

Basic models:

- User
- Post (always made by a user)

Basic features:

- user signup
- user login
- post creation
- post like
- post unlike

For User and Post objects, candidate is free to define attributes as they see fit.
Requirements:

- Token authentication (JWT is prefered)
- use Django with any other Django batteries, databases etc.


### Usage:

Create `.env` file in project root with following content:

```bash
DEBUG=True
DATABASE_URL=postgresql://db_user:secret@database:5432/blog_app
ALLOWED_HOSTS=*
JWT_SECRET_KEY=3uy49htr2vr48g76ftsk4
```

#### Run in containers:

```bash
docker-compose up --build
```

Application will start at `http://localhost:8100/`

#### Local run:

```bash
pip install pipenv && pipenv install
```

Next, update `.env` file with your `DATABASE_URL`

Enter pipenv shell:

```bash
pipenv shell
``` 

and run as usual:

```bash
./app/manage.py runserver
```

### Entrypoints

    /api/accounts/refresh/
    /api/accounts/signin/
    /api/accounts/signup/
    /api/accounts/verify/
    /api/posts/
    /api/posts/<pk>/
    /api/posts/<pk>/like/
    /api/posts/<pk>/unlike/
    /admin/

Sample requests: `./requests/`