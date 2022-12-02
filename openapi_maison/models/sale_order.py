# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def get_order_info(self):
        info = []
        for order in self:
            line_info = []
            for line in order.order_line:
                line_info.append({
                    "product_id": line.product_id.id,
                    "product_uom_qty": line.product_uom_qty,
                    "price_unit": line.price_unit
                })
            info.append({
                    "id": order.id,
                    "name": order.name,
                    "order_line": line_info
                })
        return info
