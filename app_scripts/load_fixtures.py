import os
from dotenv import load_dotenv
from app import app
from argon2 import PasswordHasher
import app_init
load_dotenv()

app.config.from_object('config.default')
app.config.from_object(os.environ.get('CONFIG_FILE'))
app.app_context().push()
app_init.init_app()

from services.database import db
from models.user import ModelUser, ModelRole, ModelUsersModelRoles

db.drop_all()
db.create_all()

ph = PasswordHasher()

role_admin = ModelRole(name='admin', label='Admin')
role_user = ModelRole(name='user', label='User')

# Roles
db.session.add(role_admin)
db.session.add(role_user)

db.session.commit()

# Users
user_admin = ModelUser(email='admin@admin.com', password=ph.hash('admin'))
user_normal = ModelUser(email='user@user.com', password=ph.hash('user'))

user_admin.roles.append(role_admin)
user_admin.roles.append(role_user)
user_normal.roles.append(role_user)

db.session.add(role_admin)
db.session.add(role_user)

db.session.commit()

print('FIXTURES LOADED')
