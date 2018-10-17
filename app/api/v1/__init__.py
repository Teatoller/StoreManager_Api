from flask import Blueprint
from flask_restful import Api

# Register blueprint application

from app.api.v1.views.products import Product, ProductList
from app.api.v1.views.sales import Sale, SaleList


version_1 = Blueprint('api', __name__, url_prefix="/api/v1")
api = Api(version_1)

api.add_resource(ProductList, '/product')
api.add_resource(Product, '/products/<int:prod_id>')

api.add_resource(SaleList, '/sale')
api.add_resource(Sale, '/sales/<int:sale_id>')