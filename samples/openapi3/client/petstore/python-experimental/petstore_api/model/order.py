# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401

from frozendict import frozendict  # noqa: F401

from decimal import Decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from petstore_api.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    DateSchema,
    DateTimeSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    InstantiationMetadata,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    NumberBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class Order(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
    id (int,): 
    petId (int,): 
    quantity (int,): 
    shipDate (datetime,): 
    status (str,): Order Status
    complete (bool,): 
    _additional_properties (Schema): the definition used for additional properties
        that are not defined in _properties
    """
    id = Int64Schema
    petId = Int64Schema
    quantity = Int32Schema
    shipDate = DateTimeSchema
    
    
    class status(
        _SchemaEnumMaker(
            enum_value_to_name={
                "placed": "PLACED",
                "approved": "APPROVED",
                "delivered": "DELIVERED",
            }
        ),
        StrSchema
    ):
        
        @classmethod
        @property
        def PLACED(cls):
            return cls._enum_by_value["placed"]("placed")
        
        @classmethod
        @property
        def APPROVED(cls):
            return cls._enum_by_value["approved"]("approved")
        
        @classmethod
        @property
        def DELIVERED(cls):
            return cls._enum_by_value["delivered"]("delivered")
    complete = BoolSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        id: typing.Union[id, Unset] = unset,
        petId: typing.Union[petId, Unset] = unset,
        quantity: typing.Union[quantity, Unset] = unset,
        shipDate: typing.Union[shipDate, Unset] = unset,
        status: typing.Union[status, Unset] = unset,
        complete: typing.Union[complete, Unset] = unset,
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
        **kwargs: typing.Type[Schema],
    ):
        return super().__new__(
            cls,
            *args,
            id=id,
            petId=petId,
            quantity=quantity,
            shipDate=shipDate,
            status=status,
            complete=complete,
            _instantiation_metadata=_instantiation_metadata,
            **kwargs,
        )