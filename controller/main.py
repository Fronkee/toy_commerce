
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json
import logging

from datetime import datetime
from werkzeug.exceptions import Forbidden, NotFound
from werkzeug.urls import url_decode, url_encode, url_parse

from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.fields import Command
from odoo.http import request, route
from odoo.addons.base.models.ir_qweb_fields import nl2br_enclose
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.payment import utils as payment_utils
from odoo.addons.payment.controllers import portal as payment_portal
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.website.models.ir_http import sitemap_qs2dom
from odoo.exceptions import AccessError, MissingError, ValidationError
from odoo.addons.portal.controllers.portal import _build_url_w_params
from odoo.addons.website.controllers import main
from odoo.addons.website.controllers.form import WebsiteForm
from odoo.addons.sale.controllers import portal as sale_portal
from odoo.osv import expression
from odoo.tools import lazy, str2bool
from odoo.tools.json import scriptsafe as json_scriptsafe

class WebsiteSale(payment_portal.PaymentPortal):
    # @http.route('/shop/payment', type='http', auth='public', website=True, sitemap=False)
    # def shop_payment(self, **post):
    #     order = request.website.sale_get_order()
    #     if order and (request.httprequest.method == 'POST' or not order.carrier_id):
    #         # Update order's carrier_id (will be the one of the partner if not defined)
    #         # If a carrier_id is (re)defined, redirect to "/shop/payment" (GET method to avoid infinite loop)
    #         carrier_id = post.get('carrier_id')
    #         keep_carrier = post.get('keep_carrier', False)
   

    #         if keep_carrier:
    #             keep_carrier = bool(int(keep_carrier))
    #         if carrier_id:
    #             carrier_id = int(carrier_id)
    #         order._check_carrier_quotation(force_carrier_id=carrier_id, keep_carrier=keep_carrier)
    #         if carrier_id:
    #             return request.redirect("/shop/payment")
    #     if request.httprequest.method == 'POST':
    #         state_id = post.get('state')
    #         print("state id is ============================",state_id)
     
    #     redirection = self.checkout_redirection(order) or self.checkout_check_address(order)
    #     if redirection:
    #         return redirection

    #     render_values = self._get_shop_payment_values(order, **post)
    #     render_values['only_services'] = order and order.only_services or False

    #     if render_values['errors']:
    #         render_values.pop('payment_methods_sudo', '')
    #         render_values.pop('tokens_sudo', '')

    #     state = request.env['deli.price'].sudo().search([])
    #     region = request.env['deli.region'].sudo().search([])
    #     render_values.update({
    #         'state':state,
    #         'region':region,
    #     })
    #     print("coming post method ===============================",region)

    #     return request.render("website_sale.payment", render_values)
        
    @http.route('/shop/final', type='http', auth='public', website=True, sitemap=False)
    def shop_final(self,**post):
        super(WebsiteSale,self).shop_payment_validate()
        super(WebsiteSale,self).shop_payment_confirmation()
        print("Post method ----------------------------",post)
        sale_order_id = request.session.get('sale_last_order_id')
        if sale_order_id:
            order = request.env['sale.order'].sudo().browse(sale_order_id)
            order.write({
                'state_id':int(post.get('state')),
                'region_id':int(post.get('region')),
                'condition':post.get("condition")
            })
            order.action_confirm()

            print("Last sale order id is ",sale_order_id,order)
            return request.redirect('/shop')

            # values = self._prepare_shop_payment_confirmation_values(order)
            # print("I am working =======================",values)

            # return request.render("website_sale.confirmation", values)
        else:
            return request.redirect('/shop')

