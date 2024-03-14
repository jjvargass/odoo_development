#!/usr/bin/python3
#coding: utf-8


class CargueTools():
    def __init__(self, odoo_client, _logger):
        self.odoo_client = odoo_client
        self._logger = _logger

    def get_user(self, login=None, name=None):
        if name:
            user = self.odoo_client.model('res.users').get([('name','=',name.strip())])
        elif login:
            user = self.odoo_client.model('res.users').get([('login','=',login.strip())])
        return user

    # contacto
    def create_find_res_partner(self, is_company=False, parent_id=None, name='', street='', phone='', mobile='', email='', website='', function=''):
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
        if not res_partner:
            self._logger.info('No Existe Contacto: ' + name + '- Se Procede a Crear')
            res_partner = self.odoo_client.model('res.partner').create({
                'is_company': is_company,
                'parent_id' : parent_id,
                'name': name.strip(),
                'street': street.strip(),
                'phone': phone.strip(),
                'mobile': mobile.strip(),
                'email': email.strip(),
                'website': website.strip(),
                'country_id': colombia.id,
                'state_id': bogota.id,
                'function': function,
            })
        return res_partner

    def create_oportunidad(self, name='', revenue=0, probability=0.0, partner_id=0, vendedor='', prioridad='', estado='', linea_negocio='', tipo_solucion='', aliado='', estrategia='', presupuesto=''):

        # buscar usuario
        vendedor_id = self.get_user(vendedor,None)

        # estado
        estado_id = self.odoo_client.model('crm.stage').get([('name','=',estado.strip())])

        # linea de negocio
        linea_negocio_id = self.odoo_client.model('crm.lead.business.line').get([('name','=',linea_negocio.strip())])

        # tipo solucion
        tipo_solucion_id = self.odoo_client.model('crm.lead.type.solution').get([('name','=',tipo_solucion.strip())])

        # Aliado
        aliado_id = self.odoo_client.model('crm.lead.ally').get([('name','=',aliado.strip())])

        # Estrategia
        estrategia_id = self.odoo_client.model('crm.lead.strategy').get([('name','=',estrategia.strip())])

        # Presupuesto
        presupuesto_id = self.odoo_client.model('crm.lead.budget').get([('name','=',presupuesto.strip())])

        errores = ""
        if not vendedor_id:
            errores = errores + "\nEl Vendedor: " + vendedor  +" No se ha encontrado en el sistema"
        if not linea_negocio_id:
            errores = errores + "\nLa linea de negocio : " + linea_negocio + " No se ha encontrado en el sistema"
        if not tipo_solucion_id:
            errores = errores + "\nEl tipo de negoio : " + tipo_solucion + " No se ha encontrado en el sistema"
        if not aliado_id:
            errores = errores + "\nEl Alido : " + aliado + " No se ha encontrado en el sistema"
        if not estrategia_id:
            errores = errores + "\La estrategia : " + estrategia + " No se ha encontrado en el sistema"
        if not presupuesto_id:
            errores = errores + "\El presupuesto : " + presupuesto + " No se ha encontrado en el sistema"

        if errores:
            raise Exception("Error con la información suministrada para los parametos agata del CRM " + errores )


        # Crear oportunidad
        oportunidad = self.odoo_client.model('crm.lead').create({
                'name': name,
                'expected_revenue': revenue,
                'probability': probability,
                'partner_id': partner_id,
                'user_id': vendedor_id,
                'priority': prioridad,
                'stage_id': estado_id,
                'linea_negocio_id': linea_negocio_id,
                'tipo_solucion_id': tipo_solucion_id,
                'aliado_id': aliado_id,
                'estrategia_id': estrategia_id,
                'presupuesto_id': presupuesto_id,
        })
        return oportunidad
