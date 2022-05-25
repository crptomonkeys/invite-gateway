# invite-gateway
rewrite of the service behind chat.cryptomonkeys.cc


# How to run

1. clone repository
2. `pip install -r requirements.txt`
3. get recaptcha keys and fill out config.py
4. run with your favourite wsgi or uwsgi, f.e.: `gunicorn -w 4 -b 0.0.0.0:5000 app:app`
