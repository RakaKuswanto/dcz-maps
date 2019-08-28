# /run.py
import os
from src.app import create_app

def mulai(environ, start_response):
    app = os.environ['FLASK_ENV']
    # run app
    app.run()
    """Simplest possible application object"""
    data = b'Hello, World!\n'
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])

if __name__ == '__main__':
  app = os.environ['FLASK_ENV']
  # run app
  app.run()
