from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False

    from .routes import inventory_bp
    app.register_blueprint(inventory_bp, url_prefix='/inventory')

    return app
