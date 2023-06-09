#!/usr/bin/env bash
# exit on error
set -o errexit

cd server 

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

cd ..
cd client

npm install

rm -rf build
npm run build