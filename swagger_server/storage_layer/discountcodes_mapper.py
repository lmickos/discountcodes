from swagger_server.models.discount import Discount
from swagger_server.storage_layer.storage import get_resource
from swagger_server.storage_layer.storage import update_resource
from swagger_server.storage_layer.storage import search_resources
from swagger_server.storage_layer.storage import add_resource
from swagger_server.storage_layer.storage import DISCOUNTCODES_GROUP_NAME


def dicts_to_discounts(discountcodes: {int: {}})->[]:
    """ Convert a dict of many resource dicts to
        a dict of many {id:Discount DTO}."""
    return [Discount.from_dict(value) for (value) in discountcodes.values()]


def get_discountcode(id: int):
    """ Get a specific DISCOUNTCODES_GROUP_NAME code"""
    res = get_resource(COMPANY_GROUP_NAME, id)
    return res


def get_discountcodes(status: str=None, company: int=None)->{id: Discount}:
    """ Get a dict of discountcodes optionally filtered by criteria.
        :param template: Optional criteria stored as a discount code dict.
            unfiltered properties are left out or set to None
        :rtype: a dict of many {id:Discount DTO}"""
    if status is None and company_id is None:
        return dicts_to_discounts(search_resources(DISCOUNTCODES_GROUP_NAME))
    else:
        criteria = {
            'status': status,
            'company': company}
        return dicts_to_discounts(search_resources(DISCOUNTCODES_GROUP_NAME, criteria))  # noqa: E501


def new_discountcode(company_id: int, offer_id: int, code: str, creationdate,
        status: str='precreated', customerid: int=None, checksum: int=None):  # noqa: E501
    new_code_dict = {
        'company': company_id,
        'creationdate': creationdate,
        'offer_id': offer_id,
        'code': code,
        'checksum': checksum,
        'customerid': customerid,
        'status': status}
    res = add_resource(DISCOUNTCODES_GROUP_NAME, new_code_dict)
    return Discount.from_dict(res)


def modify_discountcode(discount_id: int, status: str)->Discount:
    mod = {
        'id': discount_id,
        'status': status}
    res = update_resource(DISCOUNTCODES_GROUP_NAME, mod)
    return Discount.from_dict(res)
