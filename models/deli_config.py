from odoo import models,fields,api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

class DeliCharge(models.Model):
    _name = 'deli.price'

    name = fields.Char("State")
    price = fields.Float()
    deli_regs = fields.Many2one('deli.region',string="State / Region")
class DeliRegion(models.Model):
    _name = 'deli.region'

    name = fields.Char('')