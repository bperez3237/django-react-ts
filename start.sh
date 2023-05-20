cd server
gunicorn server.wsgi:application --chdir=../client/build