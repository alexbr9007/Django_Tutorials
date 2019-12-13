# Djando Docker tutorial 

### Purpose of this repo

    The following repo has the purpose to integrate a Docker image with Django and upload it into Heroku. Creating a docker image inside of Heroku gives the possibility to add more libraries  without running into the Heroku limit of 500 MB.

### Steps to deploy a Docker image with Django into Heroku


### 1. Type the following command to apply the `sudo heroku container:login` successfully. This command provides the login to connect into the Heroku Container Registry.

    `sudo apt install gnupg2 pass`


### 2. Create a new project and login into the Heroku Container Registry

    `heroku login`

    `heroku create djangodocker`

    `sudo heroku container:login`

### 3. Provide the PostgreSQL database for production

    `heroku addons:create heroku-postgresql:hobby-dev -a djangodocker`

### 4. Install the postgresql dependency

    `pipenv install dj-database-url psycopg2`

### 5. Update the Django Database Settings in the `settings.py`

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }

        # Heroku settings that need to be added
        `import dj_database_url`
        `db_from_env = dj_database_url.config()`
        `DATABASES['default'].update(db_from_env)`
        `DATABASES['default']['CONN_MAX_AGE'] = 500`

### 6. Modify the `settings.py` to include the following line for rendering templates.

    `TEMPLATES = [ ....`
        `'DIRS': [os.path.join(BASE_DIR, 'templates')],`
     `..]`

### 7. Install the pipenv dependencies with the command pipenv install

### 8. Run the following command at the same level of your manage.py file (you must have your virtual environment activated to run this command with the gunicorn library installed):

    `gunicorn djangodocker.wsgi:application --bind 0.0.0.0:8888`

## 9. There should be 2 Dockerfiles, one for heroku and the other one for local testing.

    `Dockerfile.dev` - sudo docker build -t abautista/django-docker -f Dockerfile.dev .

    `Dockerfile` - sudo docker build -t abautista/django-docker-heroku -f Dockerfile .

For testing you image locally, you need to execute the command `sudo docker run -p 3000:8888 <image_id>`.

### 10. Once you have verified the image is working locally, we need to see how is the file structure of the project and based on that, we can add the new routes for the main app and modules.
                   
djangodocker 
    | Dockerfile
    | Dockerfile-local
    | Pipfile
    | Pipfile.lock
    | README.md
    | db.sqlite3
    | manage.py
    | djangodocker ---------| __init__.py
    |                       | settings.py
    |                       | urls.py
    |                       | wsgi.py
    | task -----------------| __init__.py
                            | views.py
                            | urls.py
                            | apps.py
                            | admin.py
                            | models.py
                            | tests.py
                            | migrations --------| __init__.py


### 11. Create the docker image that will be released in Heroku. Run the command at the same level of the Dockerfile.

    `sudo docker build -t abautista/django-docker-heroku .`

### 12. Push the image into Heroku (djangodocker is the name of your app)

    `sudo heroku container:push web -a djangodocker`

### 13. Release the image in heroku

    `sudo heroku container:release web -a djangodocker`

### 14. Open the heroku app to verify that it is working.

    `heroku open -a djangodocker`

### 15. Make the migrations in the Docker container after you have changed the configuration.


    `heroku run python3 manage.py migrate -a djangodocker`
    `heroku run python3 manage.py makemigrations -a djangodocker`
    `heroku run python3 manage.py create superuser`

    In case you cannot do it with the command from above use the following: 

    `heroku run bash -a djangodocker`
    `cd src`
    `python3 manage.py makemigrations`

### Additional notes

#### See the logs in Heroku in case something has failed. 

    `heroku logs -a djangodocker --tail`

#### Log into the bash of the Heroku app. 

    `heroku run bash -a djangodocker`


