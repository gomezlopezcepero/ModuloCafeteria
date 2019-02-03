# -*- coding: utf-8 -*-

from odoo import models, fields, api



class employee_order(models.Model):
    # Reglas de cada norma. Una regla puede pertenecer a varias normas"""
    _name = 'cafeteria.employee_order'

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    products_id = fields.Many2one('cafeteria.product', string='product', domain=[('state_id', '=', 'Disponible')], required=True)
    price = fields.Integer(string='Product price',  compute='_quant')
    quantity = fields.Integer(string='Product quantity')
    order_date = fields.Date(string='order_date', default=fields.Datetime.now)

    def _quant(self):
        for record in self:
            record.price = record.products_id.price * record.quantity


class product(models.Model):
    # Reglas de cada norma. Una regla puede pertenecer a varias normas"""
    _name = 'cafeteria.product'

    name = fields.Char(string='Name', size=64, required=True, translate=True)
    description = fields.Text(string='Description', required=True, translate=True)
    barcode = fields.Text(string='Barcode', required=True, translate=True)
    price = fields.Integer(string='Product price')
    quantity = fields.Integer(string='Product quantity')
    provider_id = fields.Many2one('cafeteria.provider', string='provider')
    type_id = fields.Many2one('cafeteria.type', string='type')
    state_id = fields.Many2one('cafeteria.state', string='state')
    product_id = fields.One2many('cafeteria.employee_order', 'products_id', string='products')
    expiry_date = fields.Date()

    _sql_constraints = [('name_uniq', 'unique (name)', "Title name already exists !"), ('barcode_uniq', 'unique (barcode)', "Barcode code already exists !")]




class provider(models.Model):
    # Reglas de cada norma. Una regla puede pertenecer a varias normas"""
    _name = 'cafeteria.provider'

    name = fields.Char(string='Name', size=64, required=True, translate=True)
    provider_ids = fields.One2many('cafeteria.product', 'provider_id', string='providers')

    _sql_constraints = [('name2_uniq', 'unique (name)', "Title name already exists !")]


class state(models.Model):
    # Reglas de cada norma. Una regla puede pertenecer a varias normas"""
    _name = 'cafeteria.state'

    name = fields.Char(string='Name', size=64, required=True, translate=True)
    state_id = fields.One2many('cafeteria.product', 'state_id', string='states')

    _sql_constraints = [('name3_uniq', 'unique (name)', "Title name already exists !")]


class typeProduct(models.Model):
    # Reglas de cada norma. Una regla puede pertenecer a varias normas"""
    _name = 'cafeteria.type'

    name = fields.Char(string='Name', size=64, required=True, translate=True)
    type_products_ids = fields.One2many('cafeteria.product', 'type_id', string='products')

    _sql_constraints = [('name3_uniq', 'unique (name)', "Title name already exists !")]

# class modulo_vacio(models.Model):
#     _name = 'modulo_vacio.modulo_vacio'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100