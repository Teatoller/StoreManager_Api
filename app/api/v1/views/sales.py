from flask_restful import Resource
from flask import request

SALES = []


class Sale(Resource):
    """ """

    def get(self, sale_id):
        """ GET """
        for sale in SALES:
            if sale["sale_id"] == sale_id:
                return sale, 200

        return{"sale": None}, 404

    def sale(self):
        """ POST """
        data = request.get.json()
        sale = {"sale_id": len(SALES) + 1,
                "Sale_name": data["name"],
                "sale_price": data['price']}

        SALES.append(sale)
        return(sale), 201


class SaleList(Resource):
    def get(self):
        """ """
        return{"sales": SALES}, 200
