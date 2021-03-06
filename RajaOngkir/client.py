# -*- coding: utf-8 -*-

import payload
from .exc import RajaOngkirExc
from .httpclient import HttpClient


class Client(object):
    """RajaOngkir.com REST Client"""

    CLIENT = None

    ACCOUNT_TYPE = 'starter'

    def __init__(self, apikey, account_type="starter"):
        self.ACCOUNT_TYPE = account_type
        self.CLIENT = HttpClient(apikey, self.ACCOUNT_TYPE)

    def city(self, city_id=None, province_id=None):
        """Get list of City

        :param province_id: id of province
        :type province_id: int, long
        :param city_id: id of city
        :type city_id: int, long
        """
        endpoint = 'city'

        params = {}
        if province_id:
            params.update({'province': province_id})

        if id:
            params.update({'id': city_id})

        return self.__decode(self.CLIENT.get(params, endpoint))

    def subdistrict(self, city_id, district_id=None):
        """Get list of Subdistrict, Pro Only
        :param city_id: id of city
        :type city_id: int, long
        :param district_id: id of district (kecamatan)
        :type district_id: int, long
        """
        endpoint = 'subdistrict'

        if self.ACCOUNT_TYPE != 'pro':
            raise RajaOngkirExc('You must use Pro Account to Access This Endpoint')

        params = {
            'city': city_id
        }
        if district_id:
            params.update({
                'id': district_id
            })

        return self.__decode(self.CLIENT.get(params, endpoint))

    def province(self, province_id=None):
        """Get list of Province
        :param province_id: id of province
        """
        endpoint = 'province'

        params = {} if province_id is None else {'id': province_id}

        return self.__decode(self.CLIENT.get(params, endpoint))

    def cost(self, **kwargs):
        """Get Cost

        :param kwargs: parameter, see RajaOngkir.payload.cost
        """
        endpoint = 'cost'

        if self.ACCOUNT_TYPE == 'pro':
            params = payload.cost_pro(**kwargs)
        else:
            params = payload.cost(**kwargs)

        data = self.CLIENT.post(params, endpoint)
        return self.__decode(data)

    def __decode(self, data):
        """Decode data response, LoL"""
        return data.json()


