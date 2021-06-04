# Shopping-Cart-Rest-Api

## DESCRIPTION

 -    Built a REST Api in Flask+MongoDB
 -    A RESTful Api built for serving as a Backend for a Shopping Cart.

## REQUIREMENTS

 - Python==3.8.5
 - Flask==2.0.1
 - MongoDb

## INSTALLATION INSTRUCTIONS

### 1. Clone the repo and cd into the folder

    git clone https://github.com/dvjakhar31/shopping-cart-rest-api.git && cd shopping-cart-rest-api
    
### 2. Set up virtualenv

    virtualenv env
    
### 3. Install requirements

    pip3 install requirements.txt
    
### 4. Run the api

    python3 app.py
    
    App should now be running on http://localhost:5000/api/


## For Testing (Postman)
- Postman can be used for testing !

## Available API Routes

| Routes        | Description           | 
| ------------- |:-------------:|
| `/getItems`   |Get list of all items present in the cart|
| `/getItemWithId?id=item_id`     | Get details of an item with id item_id |     
| `/addItem?item={}`| Add an item to the cart |    
| `/removeItem` | Remove an item with given id from the cart |

