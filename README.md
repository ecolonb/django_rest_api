# django_rest_api
EnvioClick Api demo



## creating virtual environment

python3 -m venv .env

activate virtual environment
source .env/bin/activate

Install requirements
pip install -r requirements.txt



this application use mysql databases
Config on "envio_click/settings.py"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'user_db',
        'PASSWORD': 'password_userdb',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


## python3 manage.py migrate
## python3 manage.py runserver
