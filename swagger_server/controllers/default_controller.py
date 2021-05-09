import connexion
import six

from swagger_server.models.company import Company  # noqa: E501
from swagger_server.models.discount import Discount  # noqa: E501
from swagger_server.models.offer import Offer  # noqa: E501
from swagger_server import util


def create_company(body):  # noqa: E501
    """create company

    Creates a company for discounts # noqa: E501

    :param body: Create a company
    :type body: dict | bytes

    :rtype: Company
    """
    if connexion.request.is_json:
        body = Company.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_discount_codes(companyid, discountid=None, results=None, instances=None):  # noqa: E501
    """create discount codes

    Creates one or more (as requested) discount codes in the system for the given company. If an account id is given the code is set to the valid state (activated). Otherwise it is put in the dormant state (precreated) and therefore available for later fetching/activation. # noqa: E501

    :param companyid: ID of the company offering discount
    :type companyid: int
    :param discountid: ID of a personal discount
    :type discountid: int
    :param results: Indicate if we want this method to return the created code object(s). False may be useful when just precreating codes
    :type results: bool
    :param instances: Number of discount codes to create
    :type instances: int

    :rtype: Discount
    """
    return 'do some magic!'


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
    return 'do some magic!'


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
    return 'do some magic!'


def search_discount_codes(start, limit, companyid=None, discountid=None, fromdate=None, todate=None, code=None):  # noqa: E501
    """search for discount codes

    By passing in the appropriate options, you can search for available discount codes in the system # noqa: E501

    :param start: Start point in result set. For paging together with limit. 0 based (first record is 0)
    :type start: int
    :param limit: maximum number of records to return
    :type limit: int
    :param companyid: ID of the company offering discount
    :type companyid: int
    :param discountid: ID of a personal discount
    :type discountid: int
    :param fromdate: define the earliest date/time of searched discounts
    :type fromdate: str
    :param todate: define the earliest date/time of searched discounts
    :type todate: str
    :param code: Discount code
    :type code: str

    :rtype: List[Discount]
    """
    return 'do some magic!'


def set_discount_status(discountid=None, status=None):  # noqa: E501
    """change discount status

    Sets status of a specific discount record. May also attach an account to the discount. # noqa: E501

    :param discountid: ID of a personal discount
    :type discountid: int
    :param status: Wished new status. If not given the account id parameter is required and status will automatically be set to valid.
    :type status: str

    :rtype: Discount
    """
    return 'do some magic!'
