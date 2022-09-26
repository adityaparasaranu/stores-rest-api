from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister, User
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = "aditya"
api = Api(app)

# uri = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
# if uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://")

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
