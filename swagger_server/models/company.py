# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Company(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, name: str=None, description: str=None):  # noqa: E501
        """Company - a model defined in Swagger

        :param id: The id of this Company.  # noqa: E501
        :type id: int
        :param name: The name of this Company.  # noqa: E501
        :type name: str
        :param description: The description of this Company.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'description': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description'
        }
        self._id = id
        self._name = name
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'Company':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Company of this Company.  # noqa: E501
        :rtype: Company
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Company.


        :return: The id of this Company.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Company.


        :param id: The id of this Company.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Company.

        Company name. Human readable.  # noqa: E501

        :return: The name of this Company.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Company.

        Company name. Human readable.  # noqa: E501

        :param name: The name of this Company.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this Company.

        A short description of the company (i7n to come)  # noqa: E501

        :return: The description of this Company.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Company.

        A short description of the company (i7n to come)  # noqa: E501

        :param description: The description of this Company.
        :type description: str
        """

        self._description = description
