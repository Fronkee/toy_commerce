from odoo import models, fields,api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state_id = fields.Many2one('deli.price', string="State/Province")
    region_id = fields.Many2one('deli.region', string="Region")
    condition = fields.Selection([('fast','Fast'),('normal','Normal')])
    deli_price = fields.Float(string="Deli Price",compute="_compute_deli")
    all_total = fields.Float(string="All Total",compute="_compute_all_totoal")

    @api.depends('state_id')
    def _compute_deli(self):
        for rec in self:
            rec.deli_price = rec.state_id.price
            rec.tax_totals['amount_total'] =  rec.tax_totals['amount_total'] + rec.deli_price
            rec.tax_totals['amount_untaxed'] =  rec.tax_totals['amount_untaxed'] + rec.deli_price
            print("recdsdflsdf=================",rec.tax_totals)

# 'amount_untaxed': 9000.0, 'amount_total': 9000.0,
    @api.depends('amount_total','deli_price')
    def _compute_all_totoal(self):
        for rec in self:
            rec.all_total = rec.amount_total + rec.deli_price

                    


















                      