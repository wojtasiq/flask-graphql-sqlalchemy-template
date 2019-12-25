from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    app = Flask(__name__)

    app.config.from_object('config.default')
    app.config.from_object(os.environ.get('CONFIG_FILE'))

    app.run()
