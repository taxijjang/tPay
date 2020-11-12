import pytest
import json
from product.models import Tag, Product, ProductOption
from rest_framework.test import APIClient, APITestCase
from product.serializers.product_serializers import ProductSerializer


class TestView(APITestCase):
    def setUp(self):
        '''
            1. 초기 product 더미 생성
        '''
        self.client = APIClient()

        request_data = {
            "name": "unittest_product_1",
            "option_set": [
                {
                    "name": "unittest_option_1",
                    "price": 1111
                },
                {
                    "name": "unittest_option_2",
                    "price": 2222
                }
            ],
            "tag_set": [
                {
                    "name": "unittest_tag_1"
                },
                {
                    "name": "unittest_tag_2"
                }
            ]
        }

        self.products = [{
            "pk": 1,
            "name": "unittest_product_1",
            "option_set": [
                {
                    "pk": 1,
                    "name": "unittest_option_1",
                    "price": 1111
                },
                {
                    "pk": 2,
                    "name": "unittest_option_2",
                    "price": 2222
                }
            ],
            "tag_set": [
                {
                    "pk": 1,
                    "name": "unittest_tag_1"
                },
                {
                    "pk": 2,
                    "name": "unittest_tag_2"
                }
            ]
        }]

        url = "/shop/products/"
        self.client.post(
            url, json.dumps(request_data), content_type='application/json'
        )

    def test_get_product(self):
        '''
            1. products list를 요청 - GET
            2. prodcuts detail을 요청 - GET
            3. 비어있는 products detail을 요청 - GET
        '''

        ## 1번
        url = "/shop/products/"
        res = self.client.get(
            url, {}, content_type="application/json"
        )
        assert res.status_code == 200
        assert json.dumps(res.data) == json.dumps(self.products)

        ## 2번
        url = "/shop/products/1/"
        res = self.client.get(
            url, {}, content_type="application/json"
        )

        assert res.status_code == 200
        assert json.dumps(res.data) == json.dumps(self.products[0])

        ## 3번
        url = "/shop/products/2/"
        res = self.client.get(
            url, {}, content_type="application/json"
        )

        check_data = {
            'name': '',
            'option_set': [],
            'tag_set': []
        }
        assert res.status_code == 200
        assert res.data == check_data

    def test_post_product(self):
        '''
            1. 새로운 product를 추가 - POST
            2. 추가된 product의 list를 확인 - GET
            3. 추가된 product의 detail을 확인 - GET
        '''

        ## 1번
        url = "/shop/products/"

        request_data = {
            "name": "unittest_product_2",
            "option_set": [
                {
                    "pk": 1,
                    "name": "unittest_option_1",
                    "price": 1111
                },
                {
                    "name": "unittest_option_3",
                    "price": 2222
                }
            ],
            "tag_set": [
                {
                    "pk": 1,
                    "name": "unittest_tag_1"
                },
                {
                    "name": "unittest_tag_3"
                }
            ]
        }

        check_data = {"pk": 2}
        check_data.update(request_data)
        check_data['option_set'][1] = {"pk": 3, "name": "unittest_option_3", "price": 3333}
        check_data['tag_set'][1] = {"pk": 3, "name": "unit_test_tag_3"}
        self.products.append(check_data)

        res = self.client.post(
            url,
            data=json.dumps(request_data),
            content_type='application/json'
        )
        assert res.status_code == 201
        assert json.dumps(res.data) == json.dumps(check_data)

        ## 2번
        url = '/shop/products/'
        res = self.client.get(
            url, {}, content_type="application/json"
        )

        self.products[0]["option_set"].pop(0)
        assert res.status_code == 200
        assert json.dumps(res.data) == json.dumps(self.products)

        ## 3번
        url = '/shop/products/2/'
        res = self.client.get(
            url, {}, content_type="application/json"
        )

        assert res.status_code == 200
        assert json.dumps(res.data) == json.dumps(check_data)

    def test_patch_product(self):
        '''
            1. 기존의 1번 product 수정 - PATCH
            2. 수정된 parouct list 조회 - GET
            3. 수정된 product detail 조회 - GET
        '''

        ## 1번
        url = '/shop/products/1/'
        request_data = {
            "pk": 1,
            "name": "unittest_product_1",
            "option_set": [
                {
                    "pk": 1,
                    "name": "unittest_option_1",
                    "price": 1111
                },
                {
                    "name": "unittest_option_3",
                    "price": 2222
                }
            ],
            "tag_set": [
                {
                    "pk": 1,
                    "name": "unittest_tag_1"
                },
                {
                    "name": "unittest_tag_3"
                }
            ]
        }

        check_data = {
            "pk": 1,
            "name": "unittest_product_1",
            "option_set": [
                {
                    "pk": 1,
                    "name": "unittest_option_1",
                    "price": 1111
                },
                {
                    "pk": 3,
                    "name": "unittest_option_3",
                    "price": 2222
                }
            ],
            "tag_set": [
                {
                    "pk": 1,
                    "name": "unittest_tag_1"
                },
                {
                    "pk": 3,
                    "name": "unittest_tag_3"
                }
            ]
        }
        res = self.client.patch(
            url, data=json.dumps(request_data), content_type="application/json"
        )
        print(res.data)

        assert res.status_code == 200
        assert json.dumps(res.data) == json.dumps(check_data)

        ## 2번

        url = '/shop/products/'
        res = self.client.get(
            url, data={}, content_type="application/json"
        )

        assert res.status_code == 200
        assert json.dumps(res.data) == json.dumps([check_data])

        ## 3번

        url = '/shop/products/1/'
        res = self.client.get(
            url, data={}, content_type="application/json"
        )

        assert res.status_code == 200
        assert json.dumps(res.data) == json.dumps(check_data)
