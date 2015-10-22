# -*- coding: utf-8 -*-
import requests
from .exc import RajaOngkirExc

class HttpClient(object):
    """HttpClient for RajaOngkir"""

    BASEURL = "http://rajaongkir.com/api/{account_type}/{endpoint}"

    PRO_BASEURL = 'http://pro.rajaongkir.com/api/{endpoint}'

    API_KEY = None

    ENDPOINT = None

    ACCOUNT_TYPE = ''

    API_URL = None

    def __init__(self, apikey, account_type = 'starter', endpoint = None):
        self.API_KEY = apikey
        self.ENDPOINT = endpoint

        account_type = account_type.lower()
        if account_type != 'pro':
            self.API_URL = self.BASEURL.format(account_type=account_type)
        else:
            self.API_URL = self.PRO_BASEURL

    @property
    def baseurl(self):
        return self.BASEURL

    @baseurl.setter
    def baseurl(self, value):
        self.BASEURL = value

    @property
    def endpoint(self):
        return self.ENDPOINT

    @endpoint.setter
    def endpoint(self, value):
        self.ENDPOINT = value

    def get(self, query=[], endpoint=None):
        """Perform GET Request"""
        self.ENDPOINT = endpoint or self.ENDPOINT
        if not self.ENDPOINT:
            raise RajaOngkirExc("Endpoint is Missing")

        #: build api url
        url = self.API_URL.format(endpoint=self.ENDPOINT)

        #: perform request
        return requests.get(
            url,
            params=query,
            headers=self._genHeader()
        )

    def post(self, form={}, endpoint=None):
        self.ENDPOINT = endpoint or self.ENDPOINT
        if not self.ENDPOINT:
            raise RajaOngkirExc("Endpoint is Missing")

        if not isinstance(form, dict):
            raise RajaOngkirExc("Payload must be in dict.")

        #: build api url
        url = self.API_URL.format(endpoint=self.ENDPOINT)

        #: perform request
        return requests.post(
            url,
            data=form,
            headers=self._genHeader(post=True)
        )

    def _genHeader(self, post=False):
        h = {
            'key': self.API_KEY
        }

        if post:
            h.update({
                'content-type': "application/x-www-form-urlencoded"
            })

        return h
