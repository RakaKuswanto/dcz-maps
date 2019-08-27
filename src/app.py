#src/app.py

from flask   import Flask
from flask_cors import CORS
from .config import app_config
from .models import db

# import user_api blueprint
from .views.UserView                  import user_api     as user_blueprint

def create_app(env_name):
  # Create app

  # app initiliazation
  app = Flask(__name__)
  cors = CORS(app) #enable Cross Origin Resource Sharing (CORS)

  #-------------------------------------------------------------------------
  app.config.from_object(app_config['development'])
  #-------------------------------------------------------------------------

  # initializing db
  db.init_app(app)
  #-------------------------------------------------------------------------

  # register blueprint / api endpoint url 
  app.register_blueprint(user_blueprint,        url_prefix='/api/v1/users')
  #-------------------------------------------------------------------------

  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return 'WELCOME TO API SERVER PYTHON USING FLASK'
  #-------------------------------------------------------------------------

  return app
