from flask import Flask

from app.dashboard import dashboard

def create_server():
    
    server = Flask(__name__)
    
    # Dashboard
    dashboard(server)
    
    # API
    # from app.api.routes import api_blueprint
    # server.register_blueprint(api_blueprint,url_prefix='/api/v1')

    return server