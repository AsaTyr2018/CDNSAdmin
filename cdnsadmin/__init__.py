from flask import Flask


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    # Register blueprints for modular functionality
    from . import zones
    from . import corefile
    from . import plugins
    from . import backend

    app.register_blueprint(zones.bp)
    app.register_blueprint(corefile.bp)
    app.register_blueprint(plugins.bp)
    app.register_blueprint(backend.bp)

    @app.route('/')
    def index():
        return "CDNSAdmin is up and running"

    return app
