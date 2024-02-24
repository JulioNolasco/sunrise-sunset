# app.py
from flask import Flask
from app.routes import sun_info_routes

app = Flask(__name__)

app.register_blueprint(sun_info_routes)

if __name__ == '__main__':
    app.run(debug=True)
