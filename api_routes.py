from bson.objectid import ObjectId
from flask import Blueprint
from flask.globals import request
from flask.json import jsonify
from bson import ObjectId

api_routes_bp = Blueprint('api_routes', __name__)

@api_routes_bp.route('/')
def home():
  return "<h1>api works</h1>"

# Import db from app
from app import db

# Get all the items present in the cart
@api_routes_bp.route('/getItems/')
def get_items():
  items = []
  for item in db.items.find():
    item['_id'] = str(item['_id'])
    items.append(item)
  result = {"count": len(items), "items": items}
  return jsonify(result)

# Find an item using given id
@api_routes_bp.route('/getItemWithId')
def get_item():
  if "id" in request.args:
    id = request.args["id"]
    id = str(id)
    result = {}
    if not ObjectId.is_valid(id):
      result["message"] = "Not a valid id"
      return jsonify(result)
    item = db.items.find_one({"_id": ObjectId(id)})
    if item == None:
      result["message"] = "No item present with that id"
      return jsonify(result)
    result["message"] = "Successfully found an item with that id"
    result["item"] = str(item)
    return jsonify(result)
  else:
    return jsonify(message="Please provide an id")


# Add an item to the cart
@api_routes_bp.route('/addItem')
def add_item():
  if "item" in request.args:
    item = request.args["item"]
    item = eval(item)
    db.items.insert_one(item)
    result = {}
    result["item"] = str(item)
    result["message"] = "Item successfully added to the cart"
    return jsonify(result)
  else:
    return jsonify(message="No item provided to add")

# Remove item with given id from the cart
@api_routes_bp.route('/removeItem')
def remove_item():
  if "id" in request.args:
    result = {}
    id = request.args["id"]
    id = str(id)
    item = db.items.find_one_and_delete({"_id": ObjectId(id)})
    if item == None:
      result["message"] = "No item present with that id"
      return jsonify(result)
    return jsonify(message="Item removed successfully")
  else:
    return jsonify(message="No item id is provided to delete")