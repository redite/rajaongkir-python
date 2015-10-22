# -*- coding: utf-8 -*-
from exc import RajaOngkirExc

"""
    Just a Payload Builder
"""

_SUPPORTED_TYPE = ['city', 'subdistrict']
_SUPPORTED_COURIER = ['jne', 'pos', 'tiki', 'rpx', 'esl', 'pcp']

def cost(**kwargs):
    origin = kwargs.get('origin')
    destination = kwargs.get('destination')
    weight = kwargs.get('weight')
    courier = kwargs.get('courier', 'jne')

    if not origin or not destination or not weight:
        raise RajaOngkirExc("Mandatory Parameter is Missing.")

     #: check courier
    if courier not in _SUPPORTED_COURIER:
        raise RajaOngkirExc(
            "Invalid Courier Code: {0}. Available: {1}".format(
                courier,
                ", ".join(_SUPPORTED_COURIER)
            )
        )

    payload = {
        'origin': str(origin),
        'destination': str(destination),
        'weight': weight * 1000,  #: n * 1000 gram = kilo
        'courier': courier,
    }

    return payload

def cost_pro(**kwargs):

    payload = cost(**kwargs)

    origin_type = kwargs.get('originType', 'city')
    destination_type = kwargs.get('destinationType', 'city')
    length = kwargs.get('length', None)
    width = kwargs.get('width', None)
    height = kwargs.get('height', None)
    diameter = kwargs.get('diameter', None)

    #: check origin & destination type
    if (origin_type not in _SUPPORTED_TYPE) or (destination_type not in _SUPPORTED_TYPE):
        raise RajaOngkirExc(
            "Invalid Supported Type. Available: {0}".format(
                ", ".join(_SUPPORTED_TYPE)
            )
        )

    #: required payload
    payload.update({
        'originType': origin_type,
        'destinationType': destination_type,
    })

    #: optional
    if height:
        payload['height'] = height
    if width:
        payload['width'] = width
    if length:
        payload['length'] = length
    if diameter:
        payload['diameter'] = diameter

    return payload
