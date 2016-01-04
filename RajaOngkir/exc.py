# -*- coding: utf-8 -*-


class RajaOngkirExc(Exception):
    def __init__(self, message):
        self.message = message
        super(RajaOngkirExc, self).__init__(message)
