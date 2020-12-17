from flask import Flask


# name application for deploying to EB
#pass in the static files directory to avoid problems with deploying application
application = Flask(__name__, static_url_path='/app/static')

#secret key for authentication
application.config["SECRET_KEY"] = "69f0386d3078f92207ba280c371bb2ae7c321c2b9192f1626a"

#include at end to avoid circular inputs
from app import routes