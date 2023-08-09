import docker
from flask import request
from flask_restful import Resource
from http import HTTPStatus
import json
import requests
from pprint import pprint

client = docker.from_env()

class Root(Resource):
    """Root resource class to confirm root connection"""

    def get(self):
        try:
            message = {"status": "connected"}
            return message, HTTPStatus.OK
        except Exception as e:
            return e, HTTPStatus.NOT_FOUND

class Logs(Resource):
    "get container logs"

    def get(self, id):
        try:
            container = client.containers.get(id)
            logs = container.logs().decode('utf-8').splitlines()
            # compaction_logs = [line for line in logs if 'compaction' and 'Finished' in line and 'c:#' not in line]
            compaction_logs = [line for line in logs if 'compaction' in line]
            pprint(compaction_logs)
            return {"compaction_logs": compaction_logs}, HTTPStatus.OK
        except Exception as e:
            return {"error": e}, HTTPStatus.NOT_FOUND
