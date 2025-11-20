# DockerDjango

## Frequently used commands
```sh
docker-compose up
docker exec -it django /bin/bash
python ./djangotutorial/manage.py runserver 0.0.0.0:8000
python ./djangotutorial/manage.py test polls
```

## Command Usage History
```sh
docker-compose up
docker ps

docker exec -it django /bin/bash

django-admin startproject mysite djangotutorial
django-admin startapp polls

python manage.py runserver 0.0.0.0:8000

python manage.py migrate
python manage.py makemigrations polls
python manage.py sqlmigrate polls 0001
python manage.py migrate

python manage.py createsuperuser

python manage.py test polls
```

## Development environment server
http://localhost:8000/

