# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _get_pos_users(self):
        pos_users = self.env['res.users'].search_read([('groups_id', 'in', self.config_id.group_pos_user_id.id)],
                                                      ['id', 'name'])
        return pos_users

    def _get_gender_selection(self):
        field = self.env['ir.model.fields'].search([('model', '=', 'res.partner'), ('name', '=', 'gender')])
        gender_selection = self.env['ir.model.fields.selection'].search_read([('field_id', '=', field.id)],
                                                                             ['id', 'value'])
        return gender_selection

    def _pos_data_process(self, loaded_data):
        super()._pos_data_process(loaded_data)
        if self.config_id.module_pos_maison:
            loaded_data['pos_users'] = self._get_pos_users()
            loaded_data['gender_selection'] = self._get_gender_selection()

    def _loader_params_res_partner(self):
        result = super()._loader_params_res_partner()
        result['search_params']['fields'].extend(['gender', 'birthday'])
        return result
