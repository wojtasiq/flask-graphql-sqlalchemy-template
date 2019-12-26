import os
from dotenv import load_dotenv
import initialize

load_dotenv()

app = initialize.init_app()

if __name__ == "__main__":
    app.config.from_object('config.default')
    app.config.from_object(os.environ.get('CONFIG_FILE'))

    app.run()
