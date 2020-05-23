import os

from flask import Flask

# defining the application factory
def create_app(test_config=None):
    # creating and configuring the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        # loading instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # loading the config file if its passed
        app.config.from_mapping(test_config)
    
    # ensuring instance folder exists
    try:
        os.makedirs(app.instance_path)  
    except OSError:
        pass

    from flaskr import db
    db.init_app(app)
    
    from flaskr import auth, blog
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app
