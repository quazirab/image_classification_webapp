from flask import Flask

from app.dashboard import dashboard


def create_server():

    server = Flask(__name__)

    # Dashboard
    dashboard(server)

    return server
