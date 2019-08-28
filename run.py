# /run.py
import os
from src.app import create_app

if __name__ == '__main__':
  app = os.environ['FLASK_ENV']
  # run app
  app.run()
