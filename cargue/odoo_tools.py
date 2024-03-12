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

    # contacto
    def create_find_res_partner(self, is_company=False, name='', street='', phone='', mobile='', email='', website=''):
        res_partner = self.odoo_client.model('res.partner').get([
            ('name','=',name.strip()),
            ('is_company','=', is_company)
        ])
        # pais
        colombia = self.odoo_client.model('res.country').get([
            ('name','=','Colombia'.strip()),
            ('code','=', 'CO')
        ])
        # Ciudad
        bogota = self.odoo_client.model('res.country.state').get([
            ('country_id','=', colombia.id),
            ('code','=', 'DC')
        ])
        self._logger.info(colombia)
        if not res_partner:
            self._logger.info('No Existe Contacto: ' + name + '- Se Procede a Crear')
            res_partner = self.odoo_client.model('res.partner').create({
                'is_company': is_company,
                'name': name.strip(),
                'street': street.strip(),
                'phone': phone.strip(),
                'mobile': mobile.strip(),
                'email': email.strip(),
                'website': website.strip(),
                'country_id': colombia.id,
                'state_id': bogota.id,
            })
        return res_partner
        
