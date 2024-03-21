#!/usr/bin/python3
#coding: utf-8

import logging
import argparse
import erppeek

from cargue_tools import CargueTools
from crm.cargue_crm_agata import CargueCrmAgata

logging.basicConfig(level=logging.DEBUG)
_logger = logging.getLogger('cargue')

def get_conection(options):
    server = options.host_odoo + ':' + options.port_odoo
    return erppeek.Client(server, options.db_name, options.db_user, options.db_password)

def main():
    parser = argparse.ArgumentParser(description='Cargue Masivo Odoo.')

    parser.add_argument('-n', '--db_name',     dest='db_name',     help='Odoo database name', required=True)
    parser.add_argument('-u', '--db_user',     dest='db_user',     help='Odoo database user', required=True)
    parser.add_argument('-p', '--db_password', dest='db_password', help='Odoo database password', required=True)
    parser.add_argument('-f', '--file_name',    dest='file_name',    help='name of file csv for upload', required=True)
    parser.add_argument('-j', '--host_odoo',   dest='host_odoo',   help='Odoo server host', default='http://localhost')
    parser.add_argument('-k', '--port_odoo',   dest='port_odoo',   help='Odoo server port', default='8069')

    options = parser.parse_args()
    odoo_client = get_conection(options)

    _logger.info("######################################")
    _logger.info("########## Cargue Masivo #############")
    _logger.info("######################################")

    # cargue_crm_agata = CargueCrmAgata(odoo_client, _logger, options)
    # cargue_crm_agata.open_file_crm_agata()

    # cargue_tools = CargueTools(odoo_client, _logger)
    # cargue_tools.eliminar_all_oportunidad()

    # EMPLEADOS
    cargue_tools = CargueTools(odoo_client, _logger)
    cargue_tools.buscar_actualizar_hr_employee()


    _logger.info("######################################")
    _logger.info("####### Fin Cargue Masivo ############")
    _logger.info("######################################")

if __name__ == '__main__':
    main()
