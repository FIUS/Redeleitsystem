from flask import Flask, g, current_app, request, session, flash, redirect, url_for, abort, render_template, Response
from flask_login import login_user, logout_user, login_required, current_user
from flask_principal import Principal, Identity, AnonymousIdentity, identity_changed, identity_loaded, UserNeed, RoleNeed
from flask_script import Manager, prompt, prompt_pass
from flask_migrate import Migrate, MigrateCommand
from passlib.hash import pbkdf2_sha256

import config
from shared import db, login_manager
from utils import render_layout
from models.forms import LoginForm, NewUserForm
from models.database import User, Statement, Speaker, Topic, Event

app = Flask(__name__)
app.config.from_object(config)

with app.test_request_context():
    db.init_app(app)
    db.create_all()
    admin_hashed_pw = pbkdf2_sha256.encrypt("123456789", rounds=200000, salt_size=16)
    u = User("ToBeDeleted", "Standardadmin", admin_hashed_pw, ["admin", "user"])
    db.session.add(u)
    db.session.commit()