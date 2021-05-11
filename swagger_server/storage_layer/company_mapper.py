from swagger_server.models.company import Company
from swagger_server.storage_layer.storage import get_resource
# from swagger_server.storage_layer.storage import get_resources
from swagger_server.storage_layer.storage import search_resources
from swagger_server.storage_layer.storage import add_resource
from swagger_server.storage_layer.storage import COMPANY_GROUP_NAME

# Not needed due to class helper methods from_dict & to_dict
# def company_to_dict(company:Company)->{}:
#    """ Convert a Company DTO to a resource dict."""
#    return {'id':company.id, 'name':company.name, 'description':company.description}  # noqa: E501
# def dict_to_company(company:{})->{}:
#    """ Convert a resource dict to a Company DTO."""
#    return Company(id=company['id'], name=company['name'], description=company['description'])  # noqa: E501


def dicts_to_companies(companies: {int: {}})->{}:
    """ Convert a dict of many resource dicts to
        a dict of many {id:Company DTO}."""
    return {id: Company.from_dict(value) for (id, value) in companies.items()}
    # return {id: dict_to_company(value) for (id, value) in companies.items()}


def get_company(id: int):
    """ Get a specific Company"""
    res = get_resource(COMPANY_GROUP_NAME, id)
    return res


def get_companies(template: {}=None)->{id: Company}:
    """ Get a dict of companies optionally filtered by criteria.
        :param template: Optional criteria stored as a Company dict.
            unfiltered properties are left out or set to None
        :rtype: a dict of many {id:Company DTO}"""
    if template is None:
        return dicts_to_companies(search_resources(COMPANY_GROUP_NAME))
    else:
        return dicts_to_companies(search_resources(COMPANY_GROUP_NAME, template))  # noqa: E501


def new_company(company: Company):
    add_resource(COMPANY_GROUP_NAME, company.to_dict())
