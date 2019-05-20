# Starnavi TestTask

### Usage:

Create `.env` file in project root with following content:

```bash
DEBUG=True
DATABASE_URL=postgresql://starnavi_user:secret@database:5432/starnavi_app
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