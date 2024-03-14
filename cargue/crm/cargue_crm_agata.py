#!/usr/bin/python3
#coding: utf-8

import csv


class CargueCrmAgata():
    def __init__(self, odoo_client, _logger, options):
        self.odoo_client = odoo_client
        self._logger = _logger
        self.options = options

    def open_crm_agata(self):
        