from flask import Flask
from flask import redirect
from flask import render_template
from utils import Disc
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
import config

DEBUG = False
SECRET_KEY = config.secret

RECAPTCHA_PUBLIC_KEY = config.recaptcha_pub
RECAPTCHA_PRIVATE_KEY = config.recaptcha_priv

app = Flask(__name__)
app.config.from_object(__name__)

invite_client = Disc()

class InviteForm(FlaskForm):

    recaptcha = RecaptchaField()


@app.route("/")
def index(form=None):
    if form is None:
        form = InviteForm()
    return render_template("index.html", form=form)


@app.route("/verify/", methods=("POST",))
def grab_invite():

    form = InviteForm()
    if form.validate_on_submit():
        invite = invite_client.create_invite(config.target_discord_server_id).json()
        return redirect(invite["url"])
    return index(form)

