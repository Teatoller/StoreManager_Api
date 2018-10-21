class ProductModel():
    """ """
    product_id = 1

    def __init__(self, name, price, quantity, category):
        self.product_id = ProductModel.product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        ProductModel.product_id += 1

    def resultant(self):
        """ """
        return dict(
            product_name=self.name,
            product_price=self.price,
            product_quantity=self.quantity,
            product_category=self.category
        )


class ListDatabase():
    PRODUCTS = []
    SALES = []

    @classmethod
    def get_product_id(cls, product_id):
        for p in cls.PRODUCTS:
            if p.product_id == product_id:
                return p

    @classmethod
    def get_product_by_name(cls, name):
        for p in cls.PRODUCTS:
            if p.name == name:
                return p
