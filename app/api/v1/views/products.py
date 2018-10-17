from flask_restful import Resource
from flask import request

PRODUCTS = []


class Product(Resource):
    """ """

    def get(self, prod_id):
        """ GET """
        for product in PRODUCTS:
            if product["product_id"] == prod_id:
                return product, 200

        return {"product": None}, 404

    def post(self):
        """ POST """
        data = request.get.json()
        product = {"product_id": len(PRODUCTS) + 1,
                   "Product_name": data["name"],
                   "product_price": data['price']}

        PRODUCTS.append(product)
        return(product), 201


class ProductList(Resource):
    def get(self):
        """ """
        return{"products": PRODUCTS}, 200
