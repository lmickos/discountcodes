import connexion
import six

from swagger_server.models.company import Company  # noqa: E501
from swagger_server.models.discount import Discount  # noqa: E501
from swagger_server.models.offer import Offer  # noqa: E501
from swagger_server import util

from swagger_server.models.company import Company
from swagger_server.storage_layer.company_mapper import get_companies
from swagger_server.storage_layer.company_mapper import new_company
from swagger_server.storage_layer.discountcodes_mapper import new_discountcode
from swagger_server.storage_layer.discountcodes_mapper import get_discountcodes    # noqa: E501
from swagger_server.storage_layer.discountcodes_mapper import modify_discountcode  # noqa: E501

import random
import string
from datetime import datetime


def create_company(body):  # noqa: E501
    """create company

    Creates a company for discounts # noqa: E501

    :param body: Create a company
    :type body: dict | bytes

    :rtype: Company
    """
    if connexion.request.is_json:
        body = Company.from_dict(connexion.request.get_json())  # noqa: E501
        new_company(body)
        return 'Success', 201
    else:
        return 'invalid input, could not create company', 400


def create_discount_codes(companyid, accountid=None, results=None, instances=None):  # noqa: E501
    """create discount codes

    Creates one or more (as requested) discount codes in the system for the given company. If an account id is given the code is set to the valid state (activated). Otherwise it is put in the dormant state (precreated) and therefore available for later fetching/activation. # noqa: E501

    :param companyid: ID of the company offering discount
    :type companyid: int
    :param accountid: ID of a personal discount
    :type accountid: int
    :param results: Indicate if we want this method to return the created code object(s). False may be useful when just precreating codes
    :type results: bool
    :param instances: Number of discount codes to create
    :type instances: int

    :rtype: List[Discount]
    """
    created_codes = []
    new_disc = Discount()
    # Iterate as many times as requested
    for i in range(instances):
        code = generate_code(16)  # A random code unlikely to collide, but not guaranteed unique  # noqa: E501
        hash = random.randrange(10000)  # Let's fake a hash for now
        # Handle properties dor the new discount code
        offer_id = 0  # Fake offer id for now
        creation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if accountid is None:
            status = 'precreated'
        else:
            status = 'valid'
        # Create the discount code
        new_code = new_discountcode(companyid, offer_id, code, creation, status, accountid, hash)  # noqa: E501
        created_codes.append(new_code)
    if results:
        return created_codes  # Should be an array of results
    else:
        return None, 400


def generate_code(length: int=16)->str:
    """ A random code generator for a wished number of characters.
        Todo: Move to a util class"""
    from_chars = string.ascii_uppercase
    result = ''.join(random.choice(from_chars) for i in range(length))
    return result


def create_offer(body, companyid):  # noqa: E501
    """create offer

    Creates a discount offer # noqa: E501

    :param body: Create an offer with the given parameters
    :type body: dict | bytes
    :param companyid: ID of the company offering discount
    :type companyid: int

    :rtype: Offer
    """
    if connexion.request.is_json:
        body = Offer.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def fetch_discount_code(companyid, accountid):  # noqa: E501
    """fetch precreated discount code

    Fetch a precreated unused discount code for a given account Creates one or more (as requested) discount codes in the system for the given company # noqa: E501

    :param companyid: ID of the company offering discount
    :type companyid: int
    :param accountid: Account id for the fetched discount code
    :type accountid: int

    :rtype: Discount
    """
    pre_list = get_discountcodes(status='precreated')
    print(pre_list, len(pre_list))
    if len(pre_list) == 0:
        return 'No precreated unused codes available', 500
    else:
        activate_id = pre_list[0].id
        res = modify_discountcode(discount_id=activate_id, status='valid')
        return res


def get_company_offer(companyid, offeridpath):  # noqa: E501
    """get company offer

    Retrieves a specific offer for given company. # noqa: E501

    :param companyid: ID of the company offering discount
    :type companyid: int
    :param offeridpath: ID of discount offering
    :type offeridpath: int

    :rtype: Offer
    """
    return 'do some magic!'


def get_company_offers(companyid):  # noqa: E501
    """get company offers

    Retrieves offers for a given company. # noqa: E501

    :param companyid: ID of the company offering discount
    :type companyid: int

    :rtype: List[Offer]
    """
    return 'do some magic!'


def get_discount(discountid):  # noqa: E501
    """get personal discount

    Retrieves a specific discount record. # noqa: E501

    :param discountid: ID of a personal discount
    :type discountid: int

    :rtype: Discount
    """
    return 'do some magic!'


def search_companies(companyname=None):  # noqa: E501
    """search for companies

    Searches for companies by name. Only returns companies the user is authorized for. # noqa: E501

    :param companyname: Name of company you are looking for. Exact match. If name is not given, returns id of all found companies authorized for.
    :type companyname: str

    :rtype: List[Company]
    """
    return get_companies() if companyname is None else get_companies({'name': companyname})  # noqa: E501


def search_discount_codes(limit=100, companyid=None, accountid=None, discountid=None, fromdate=None, todate=None, code=None, start=0):  # noqa: E501
    """search for discount codes

    By passing in the appropriate options, you can search for available discount codes in the system # noqa: E501

    :param limit: maximum number of records to return
    :type limit: int
    :param companyid: ID of the company offering discount
    :type companyid: int
    :param accountid: ID of a personal discount
    :type accountid: int
    :param discountid: ID of a personal discount
    :type discountid: int
    :param fromdate: define the earliest date/time of searched discounts
    :type fromdate: str
    :param todate: define the earliest date/time of searched discounts
    :type todate: str
    :param code: Discount code
    :type code: str
    :param start: Start point in result set. For paging together with limit. 0 based (first record is 0)
    :type start: int

    :rtype: List[Discount]
    """
    return 'do some magic!'


def set_discount_status(discountid, accountid=None, status=None):  # noqa: E501
    """change discount status

    Sets status of a specific discount record. May also attach an account to the discount. # noqa: E501

    :param discountid: ID of a personal discount
    :type discountid: int
    :param accountid: ID of a personal discount
    :type accountid: int
    :param status: Wished new status. If not given the account id parameter is required and status will automatically be set to valid.
    :type status: str

    :rtype: Discount
    """
    return 'do some magic!'
