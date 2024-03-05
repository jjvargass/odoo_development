#!/usr/bin/python3
#coding: utf-8

class OdooTools():
    def __init__(self, odoo_client, _logger):
        self.odoo_client = odoo_client
        self._logger = _logger

    def get_user(self, login=None, email=None):
        if email:
            user = self.odoo_client.model('res.users').get([('name','=',email.strip())])
        elif login:
            user = self.odoo_client.model('res.users').get([('login','=',login.strip())])
        return user