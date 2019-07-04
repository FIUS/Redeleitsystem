from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_principal import Permission, RoleNeed

db = SQLAlchemy()
login_manager = LoginManager()

admin_permission = Permission(RoleNeed("admin"))
user_permission = Permission(RoleNeed("user"))
roles = ["user", "admin"]

