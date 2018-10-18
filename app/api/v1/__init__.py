from flask import Blueprint
from flask_restful import Api

# Register blueprint application

from app.api.v1.views.products import Product, Products
from app.api.v1.views.sales import Sale, Sales


version_1 = Blueprint('api', __name__, url_prefix="/api/v1")
api = Api(version_1)

# api.add_resource(ProductList, '/products/')
# api.add_resource(Product, '/products/')

api.add_resource(Products, '/products/')
api.add_resource(Product, '/products/<int:id>')


api.add_resource(Sales, '/sales')
api.add_resource(Sale, '/sales/<int:id>')
