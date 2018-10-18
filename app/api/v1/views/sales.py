from flask_restful import Resource
from flask import request
from app.api.v1.models.sales import SaleModel, ListDatabase


class Sale(Resource):
    def get(self, id):
        sale = ListDatabase.get_sale_id(id)
        if sale:
            return {"status": "success", "sale": sale.resultant()}, 200
        return {"status": "Failed!", "msg": "sale not found"}, 404


class Sales(Resource):
    def post(self):
        """ POST """
        data = request.get_json(force=True)
        if 'name' not in data:
            return {"msg": "please input name"}, 406
        if 'price' not in data:
            return {"msg": "please input price :"}, 406
        if 'quantity' not in data:
            return{"msg": "Stock is Nil"}

        sale = SaleModel(
            data['name'],
            data['price'],
            data['quantity'],
            data['category'])
        ListDatabase.SALES.append(sale)
        response = sale.resultant()
        return {"status": "success!", "sale": response}, 201

    def get(self):
        sale = [i.resultant() for i in ListDatabase.SALES]
        return {"status": "success!", "sales": sale}, 200
