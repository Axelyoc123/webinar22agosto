# -*- coding: utf-8 -*-

from odoo import models, fields #from odoo es el framework principal aqui importamos las siguientes clases,
#models=para definir los tipos de modelos
#fields para definir los tipos de campos

#estamos generando un modelo para herencia(es muy importante que este en camelcase)
class ProductTemplate(models.Model):
    _inherit='product.template' #inherit es para realizar una herencia
  
    price_2 = fields.Monetary(string="precio 2")