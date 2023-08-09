import docker
from flask import Flask

from flask_restful import Api
import requests
import httpie

from resources import Root, Logs

print("starting")

app = Flask(__name__)
api = Api(app)

api.add_resource(Root, '/')
api.add_resource(Logs, '/logs/<string:id>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    