from flask import Flask

# creating the app
def create_app():
    app = Flask(__name__)

# Use application to name our blueprint
    from app.api.v1 import version_1 as v1
    app.register_blueprint(v1)
    return app