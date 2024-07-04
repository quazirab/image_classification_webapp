import os

from app import create_server

server = create_server()

DEBUG = os.environ.get("DEBUG", "TRUE")
DEBUG = True if DEBUG.upper == "TRUE" else False

HOST_URL = os.environ.get("HOST_URL", "0.0.0.0")
HOST_PORT = int(os.environ.get("HOST_PORT", 5000))

if __name__ == "__main__":
    server.run(debug=DEBUG, host=HOST_URL, port=HOST_PORT)
