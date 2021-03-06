import os
from dotenv import load_dotenv
from app import app
import app_init
load_dotenv()

app.config.from_object('config.default')
app.config.from_object(os.environ.get('CONFIG_FILE'))
app.app_context().push()
app_init.init_app()

from services.database import db
from models.user import ModelUser, ModelRole, ModelUsersModelRoles

db.drop_all()




