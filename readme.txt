python3 -m venv env
on window
.\env\Scripts\activate
on mac
source env/bin/activate

pip install django
pip install djangorestframework
pip install djangorestframework-simplejwt
pip install django-cors-headers
python manage.py makemigrations booking_app

pip install -r requirements.txt



python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py runserver


https://18.219.110.195/admin
python manage.py createsuperuser




