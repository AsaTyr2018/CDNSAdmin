from flask import Flask
import os


def create_app():
    """Create and configure the Flask application."""
    template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
    app = Flask(__name__, template_folder=template_dir)
    app.config['SECRET_KEY'] = 'change-me'
    
    # Register blueprints for modular functionality
    from . import zones
    from . import corefile
    from . import plugins
    from . import backend
    from . import web

    app.register_blueprint(zones.bp)
    app.register_blueprint(corefile.bp)
    app.register_blueprint(plugins.bp)
    app.register_blueprint(backend.bp)
    app.register_blueprint(web.bp)


    return app
