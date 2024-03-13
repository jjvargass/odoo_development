#!/usr/bin/python3
#coding: utf-8

import logging
import argparse
import erppeek

from cargue_tools import CargueTools

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
    parser.add_argument('-w', '--file_way',    dest='file_way',    help='way o path of file csv', required=True)
    parser.add_argument('-j', '--host_odoo',   dest='host_odoo',   help='Odoo server host', default='http://localhost')
    parser.add_argument('-k', '--port_odoo',   dest='port_odoo',   help='Odoo server port', default='8069')

    options = parser.parse_args()

    odoo_client = get_conection(options)
    #_logger.info(odoo_client.common.version())

    utilidad = CargueTools(odoo_client, _logger)
    
    # usuarios
    _logger.info("Usuario========")
    usuario = utilidad.get_user("portal",None)
    _logger.info(usuario.partnet_id)

    # contacto
    _logger.info("Contacto========")
    padre_contacto = utilidad.create_find_res_partner(
        True,
        None,
        'MINTIC - Ministerio TIC',
        'Edificio Murillo Toro Cra. 8a entre calles 12A y 12B Bogotá',
        '+57 601 344 34 60',
        '',
        'minticresponde@mintic.gov.co',
        'https://www.mintic.gov.co/',
        '',
    )

    contacto = utilidad.create_find_res_partner(
        False,
        padre_contacto.id,
        'Lina Zuluaga',
        'Edificio Murillo Piso 3',
        '',
        '3102422608',
        'minticresponde@mintic.gov.co',
        'https://www.mintic.gov.co/',
        'Asesora de IA',
    )
    _logger.info(contacto)

    _logger.info("Oportunidad========")
    oportunidad = utilidad.create_oportunidad(
        'Redes Sociales JOTAAAAAAAA',
        832837311,
        20.0,
        contacto.id,
        'jose@agatadata.com',
        'Producto',
        'Redes Sociales',
        'Wise CX',
        'Nación',
        'No',
    )
    _logger.info(oportunidad)

if __name__ == '__main__':
    main()