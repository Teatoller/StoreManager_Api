class SaleModel():
    """ """
    sale_id = 1

    def __init__(self, name, price, quantity, category):
        self.sale_id = SaleModel.sale_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        SaleModel.sale_id += 1

    def resultant(self):
        """ """
        return dict(
            sale_name=self.name,
            sale_price=self.price,
            sale_quantity=self.quantity,
            sale_category=self.category
        )


class ListDatabase():
    PRODUCTS = []
    SALES = []

    @classmethod
    def get_sale_id(cls, sale_id):
        for sale in cls.SALES:
            if sale.sale_id == sale_id:
                return sale

    @classmethod
    def get_sale_by_name(cls, name):
        for sale in cls.SALES:
            if sale.name == name:
                return sale
