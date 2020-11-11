import pytest
import json
from rest_framework.test import APITestCase
from product.serializers.product_serializers import ProductSerializer


class TestView(APITestCase):
    ## 비어있는 product를 요청
    def test_get_product(self):
        '''
            1. 비어있는 products list를 요청 - GET
            2. 비어있는 prodcuts detail을 요청 - GET
        '''
        url = "/shop/products/"
        res = self.client.get(
            url,
            {},
            content_type="application/json"
        )
        assert res.status_code == 200
        assert res.data == []

        ## 비어있는 products detail을 요청 했을때
        url = "/shop/products/1"
        res = self.client.get(
            url, {}, content_type="application/json"
        )
        assert res.status_code == 301

    def test_post_product(self):
        '''
            1. 새로운 product를 추가 - POST
            2. 추가된 product의 list를 확인 - GET
            3. 추가된 product의 detail을 확인 - GET
        '''

        ## 1번
        url = "/shop/products/"

        request_data = {
            "name": "unittest",
            "option_set": [
                {
                    "name": "unittest_option",
                    "price": 777
                }
            ],
            "tag_set": [
                {
                    "name": "unittest_tag"
                }
            ]
        }

        check_data = {
            "pk": 1,
            "name": "unittest",
            "option_set": [
                {
                    "pk": 1,
                    "name": "unittest_option",
                    "price": 777
                }
            ],
            "tag_set": [
                {
                    "pk": 1,
                    "name": "unittest_tag"
                }
            ]
        }


        res = self.client.post(
            url,
            data=json.dumps(request_data),
            content_type='application/json'
        )
        assert res.status_code == 201
        assert res.data == check_data

        ## 2번
        url = '/shop/products/'
        res = self.client.get(
            url, {}, content_type="application/json"
        )

        products_data = [check_data]
        assert res.status_code == 200
        assert json.dumps(res.data) == json.dumps(products_data)

        ## 3번
        url = '/shop/products/1/'
        res = self.client.get(
            url, {}, content_type="application/json"
        )

        assert res.status_code == 200
        assert json.dumps(res.data) == json.dumps(products_data[0])

    def test_patch_product(self):
        pass