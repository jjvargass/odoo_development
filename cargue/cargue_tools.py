#!/usr/bin/python3
#coding: utf-8

import datetime
import os

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
            # self._logger.info('No Existe Contacto: ' + name + '- Se Procede a Crear')
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

    def create_oportunidad(self, name='', revenue=0, probability=0.0, partner_id=0, vendedor='', prioridad='', estado='', linea_negocio='', tipo_solucion='', aliado='', estrategia='', presupuesto='', fecha_cierre='', descripcion=''):

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

        if not fecha_cierre:
            #fecha_cierre = str(datetime.datetime.now().date())
            fecha_cierre = '2024-12-31'

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
                'date_deadline': fecha_cierre,
                'description' : descripcion,
        })
        return oportunidad


    def eliminar_all_oportunidad(self):
        oportunidades_ids = self.odoo_client.model('crm.lead').search([])
        for oportunidad in oportunidades_ids:
            self._logger.info(oportunidad)
            eliminado = self.odoo_client.model('crm.lead').get(oportunidad).unlink()

    ## hr.employee ##
    def buscar_actualizar_hr_employee(self,
            id_agata="",
            nombres_apellidos="",
            gerencia="",
            cargo="",
            correo_corporativo="",
            direccion="",
            idioma="",
            correo_personal="",
            celular="",
            estado_civil="",
            numero_hijos="",
            emergencia_nombre="",
            emergencia_cel="",
            nacionalidad="",
            numero_identificación="",
            genero="",
            fecha_nacimiento="",
            lugar_de_nacimiento="",
            pais_nacimiento="",
            tipo_de_empleado="",
            contrato_fecha_inciaio="",
            contrato_fecha_fin="",
            contrato_programa_trabajo="",
            contrato_tipo="",
            contrato_descripcion="",
        ):

        self._logger.info("hola")
        # Ruta Actual
        separador = os.path.sep  # obtiene segun el sistema operativo
        dir_actual = os.path.dirname(os.path.abspath(__file__))

        # empleado
        empleado_id = self.odoo_client.model('hr.employee').get([('work_email','=',correo_corporativo.strip())])

        # gerencia
        department_id = self.odoo_client.model('hr.department').get([('name','=',gerencia.strip())])

        # Puesto de Trabajo
        job_id = self.odoo_client.model('hr.job').get([('name','=',cargo.strip())])

        # nacionalidad
        nacionalidad_id = self.odoo_client.model('res.country').get([('name','=',nacionalidad.strip())])

        # pais_nacimiento
        pais_nacimiento_id = self.odoo_client.model('res.country').get([('name','=',pais_nacimiento.strip())])

        errores = ""
        if not empleado_id:
            self._logger.info("El empleado: " + correo_corporativo  +" No se ha encontrado en el sistema")
        if not department_id:
            errores = errores + "\nLa gerencia : " + gerencia + " No se ha encontrado en el sistema"
        if not job_id:
            errores = errores + "\nEl Puesto de trabajo : " + cargo + " No se ha encontrado en el sistema"
        if not nacionalidad_id:
            errores = errores + "\nLa macionalidad : " + nacionalidad + " No se ha encontrado en el sistema"
        if not pais_nacimiento_id:
            errores = errores + "\El pais de nacimiento  : " + pais_nacimiento + " No se ha encontrado en el sistema"

        if errores:
            raise Exception("Error con la información suministrada para los parametos agata del módulo Emepleados " + errores )

        # Actualizar empleado
        if empleado_id:
            empleado_id.write({
                'mobile_phone': celular,
                'department_id': department_id,
                'job_id': job_id,
                'marital': estado_civil,
                'children': numero_hijos,
                'emergency_contact':emergencia_nombre,
                'emergency_phone': emergencia_cel,
                'country_id':nacionalidad_id,
                'identification_id': numero_identificación,
            })