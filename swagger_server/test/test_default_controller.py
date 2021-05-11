# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.company import Company  # noqa: E501
from swagger_server.models.discount import Discount  # noqa: E501
from swagger_server.models.offer import Offer  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_company(self):
        """Test case for create_company

        create company
        """
        body = Company()
        response = self.client.open(
            '/companies',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_discount_codes(self):
        """Test case for create_discount_codes

        create discount codes
        """
        query_string = [('companyid', 789),
                        ('accountid', 789),
                        ('results', true),
                        ('instances', 10000)]
        response = self.client.open(
            '/discountcodes',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_offer(self):
        """Test case for create_offer

        create offer
        """
        body = Offer()
        query_string = [('companyid', 789)]
        response = self.client.open(
            '/offers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_fetch_discount_code(self):
        """Test case for fetch_discount_code

        fetch precreated discount code
        """
        query_string = [('companyid', 789),
                        ('accountid', 789)]
        response = self.client.open(
            '/discountcodes/precreated',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_company_offer(self):
        """Test case for get_company_offer

        get company offer
        """
        query_string = [('companyid', 789)]
        response = self.client.open(
            '/offers/{offeridpath}'.format(offeridpath=789),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_company_offers(self):
        """Test case for get_company_offers

        get company offers
        """
        query_string = [('companyid', 789)]
        response = self.client.open(
            '/offers',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_discount(self):
        """Test case for get_discount

        get personal discount
        """
        response = self.client.open(
            '/discountcodes/{discountid}'.format(discountid=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_companies(self):
        """Test case for search_companies

        search for companies
        """
        query_string = [('companyname', 'companyname_example')]
        response = self.client.open(
            '/companies',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_discount_codes(self):
        """Test case for search_discount_codes

        search for discount codes
        """
        query_string = [('companyid', 789),
                        ('accountid', 789),
                        ('discountid', 789),
                        ('fromdate', 'fromdate_example'),
                        ('todate', 'todate_example'),
                        ('code', 'code_example'),
                        ('start', 0),
                        ('limit', 100)]
        response = self.client.open(
            '/discountcodes',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_set_discount_status(self):
        """Test case for set_discount_status

        change discount status
        """
        query_string = [('accountid', 789),
                        ('status', 'status_example')]
        response = self.client.open(
            '/discountcodes/{discountid}'.format(discountid=789),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
