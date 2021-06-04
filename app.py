# Important imports
from flask import Flask
from flask_pymongo import PyMongo
from api.api_routes import api_routes_bp

# Set up app
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["MONGO_URI"] = "mongodb+srv://dvjakhar:helloworld@cluster0.ej6tm.mongodb.net/shopping_cart"

mongodb_client = PyMongo(app)
db = mongodb_client.db

# Set up api routes
app.register_blueprint(api_routes_bp, url_prefix="/api")

if __name__=="__main__":
  app.run(debug=True)