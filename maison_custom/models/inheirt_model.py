from odoo import _, api, exceptions, fields, models
from datetime import datetime, timedelta

class ResPartner(models.Model):
    _inherit = 'res.partner'

    birthday = fields.Datetime(string='Birthday')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", default="male")


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    customer = fields.Many2one('res.partner', string='Customer')
    scendy = fields.Many2one('hr.employee', string='Scendy')


