from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config
db = SQLAlchemy()
migrate = Migrate()

def index():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .views import main_view
    from . import models
    app.register_blueprint(main_view.bp)
    return app
