import os

from app import create_app

app = create_app()

if __name__ == "__main__":
    host = os.getenv("APP_HOST", "0.0.0.0")
    debug = os.getenv("APP_DEBUG", "false").lower() == "true"
    app.run(host=host, port=5000, debug=debug)
