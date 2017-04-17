drchrono Hackathon

Requirements

pip
python virtual env
Setup

$ pip install -r requirements.txt
$ python manage.py runserver
social_auth_drchrono/ contains a custom provider for Python Social Auth that handles OAUTH for drchrono. To configure it, set these fields in your drchrono/settings.py file:

SOCIAL_AUTH_DRCHRONO_KEY
SOCIAL_AUTH_DRCHRONO_SECRET
SOCIAL_AUTH_DRCHRONO_SCOPE
LOGIN_REDIRECT_URL