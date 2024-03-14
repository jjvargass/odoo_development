#!/usr/bin/python3
#coding: utf-8

import csv
import os
from cargue_tools import CargueTools


class CargueCrmAgata():
    def __init__(self, odoo_client, _logger, options):
        self.odoo_client = odoo_client
        self._logger = _logger
        self.options = options

    def open_file_crm_agata(self):
        # Ruta Actual
        separador = os.path.sep  # obtiene segun el sistema operativo
        dir_actual = os.path.dirname(os.path.abspath(__file__))

        cargue_tools = CargueTools(self.odoo_client, self._logger)

        with open(dir_actual + '/' + self.options.file_name) as csvfile:
            reader = csv.DictReader(csvfile)
            rowcount  = 0
            for row in reader:
                rowcount+= 1
                self._logger.info('Line CSV:' + str(rowcount))
                # crear cliente Compañia
                cliente_compañia = cargue_tools.create_find_res_partner(
                    True,
                    None,
                    row['cliente_compania_nombre'],
                    row['cliente_compania_direccion'],
                    row['cliente_compania_telefono'],
                    row['cliente_compania_cel'],
                    row['cliente_compania_email'],
                    row['cliente_compania_web'],
                    '',
                )
                if row['cliente_individuo_nombre']:
                    cliente = cargue_tools.create_find_res_partner(
                        False,
                        cliente_compañia.id,
                        row['cliente_individuo_nombre'],
                        row['cliente_individuo_direccion'],
                        row['cliente_individuo_telefono'],
                        row['cliente_individuo_cel'],
                        row['cliente_individuo_email'],
                        row['cliente_individuo_web'],
                        row['cliente_individuo_puesto_trabajo'],
                    )