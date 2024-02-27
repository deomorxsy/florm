from flask import Flask, make_response
from flask_cors import CORS, cross_origin
import logging

# orm routes
from app.routes.alumni_bp import blueprint as alumni_bp
from app.routes.lecture_bp import blueprint as lecture_bp
from app.routes.history_bp import blueprint as history_bp
from app.routes.ping import blueprint as ping

# session routes
#from app.user.views import blueprint as user_views_bp
#from app.public.views import blueprint as public_views_bp

# extensions
from .extensions import db


# ci env check base repo
def create_app(config_object="app.settings"):
    """ create application factory """
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)

    # print(f'from app.py: {app.app_context()}')
    # print(f'from app.py: {type(current_app.name)}')

    # swagger
    #flask_restplus_swagger(app)
    swagger_ui(app)

    # enable CORS
    #CORS(app, resources={r'/ping/': {'origins': 'http://localhost:5173'}},
    #     supports_credentials=True)
    #CORS(app, resources={r'/ping/': {'origins': '*'}})

    logging.basicConfig(level=logging.INFO)
    return app


def register_extensions(app):
    """ register flask extensions """
    db.init_app(app)

    return None


def register_blueprints(app):
    """ register flask blueprints """

    # orm REST API routes
    app.register_blueprint(alumni_bp)
    app.register_blueprint(lecture_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(ping)

    # session-cookie authentication views route
    #app.register_blueprint(user_views_bp)
    #app.register_blueprint(public_views_bp)

    return None


def swagger_ui(app):
    """ plug swagger-ui into the existing Flask API """
    from swagger_ui import api_doc

    api_doc(
            app,
            config_path='../docs/swagger-ui.yaml',
            url_prefix='/api/doc',
            title='first api doc'
            )


if __name__ == '__main__':
    create_app()[0].run(host='127.0.0.1', port=5000, debug=True)
    #print(f'hullo {type(create_app()[0])}')
