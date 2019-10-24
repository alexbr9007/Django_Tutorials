# build our heroku-ready local Docker image
sudo docker build -t abautista/django-docker-heroku -f Dockerfile .


# push your directory container for the web process to heroku
heroku container:push web -a djangodocker


# promote the web process with your container 
heroku container:release web -a djangodocker


# run migrations
#heroku run python3 src/manage.py migrate -a djangodocker
