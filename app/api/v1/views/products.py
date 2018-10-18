from flask_restful import Resource
from flask import request
from app.api.v1.models.product import ProductModel, ListDatabase


class Product(Resource):
    def get(self, id):
        product = ListDatabase.get_product_id(id)
        if product:
            return {"status": "success", "product": product.resultant()}, 200
        return {"status": "Failed!", "msg": "product not found"}, 404


class Products(Resource):
    def post(self):
        """ POST """
        data = request.get_json(force=True)
        if 'name' not in data:
            return {"msg": "please input name"}, 406
        if 'price' not in data:
            return {"msg": "please input price"}, 406
        if 'quantity' not in data:
            return {"msg": "please input quantity"}, 406
        if 'category' not in data:
            return {"msg": "please input category"}, 406 

        product = ProductModel(
            data['name'],
            data['price'],
            data['quantity'],
            data['category'])
        ListDatabase.PRODUCTS.append(product)
        res = product.resultant()
        return {"status": "success!", "product": res}, 201

    def get(self):
        ps = [i.resultant() for i in ListDatabase.PRODUCTS]
        return {"status": "succes!", "products": ps}, 200
