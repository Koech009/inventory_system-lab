"""
This module initializes the Flask application using an application factory.
It registers all blueprints (API routes) and sets configuration options.
"""
from flask import Flask


def create_app():
    """
    Create and configure a Flask app instance.
    """
    app = Flask(__name__)
    # Keep JSON keys in order
    app.config['JSON_SORT_KEYS'] = False
    from .routes import inventory_bp
    app.register_blueprint(inventory_bp, url_prefix='/inventory')

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
