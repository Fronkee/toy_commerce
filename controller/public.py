from odoo import http
from odoo.http import request
import json
class MyModuleController(http.Controller):


    @http.route('/toy_commerce/get_regions', type='json', auth='public', website=True)
    def get_regions(self):
        regions = request.env['deli.region'].sudo().search_read([], ['id', 'name'])
        return regions    
    
    @http.route('/toy_commerce/get_state_price', type='json', auth='public', website=True, method=['POST'])
    def get_states(self):
        data = json.loads(request.httprequest.data.decode())
        region_id = data['params']['region_id']
        print('Received region_id:', data)  # Log received data
        states = request.env['deli.price'].sudo().search_read([('deli_regs', '=', region_id)], ['id', 'name', 'price'])
        return states
    