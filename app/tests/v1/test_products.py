import unittest
from flask import json
from app import create_app
from app.api.v1.models.product import ListDatabase

config_name = "testing"
app = create_app(config_name)

p_url = 'api/v1/products'


class TestProduct(unittest.TestCase):
    """ """

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

        self.product_data = {
            "name": "Cabin",
            "price": 50000,
            "quantity": 1,
            "category": "delux"
        }

    def test_add_product(self):
        res = self.app.post(p_url,
                            data=json.dumps(self.product_data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_get_all_products(self):
        """ Test get method """
        self.app.post(p_url,
                      data=self.product_data,
                      content_type='application/json')
        res = self.app.get(p_url)
        self.assertEqual(res.status_code, 200)

    def test_get_single_product(self):
        """ """
        self.app.post(p_url,
                      data=self.product_data,
                      content_type='application/json')
        product = ListDatabase.get_product_by_name('Cabin')
        p_id = product.product_id
        product = self.app.get('/api/v1/products/{}'.format(p_id))
        self.assertEqual(product.status_code, 200)
