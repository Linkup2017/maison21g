# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "pos_maison",
    'category': "Hidden",
    'summary': 'Link module between Point of Sale and Maison',

    'description': """
Added client-specific information in the 'point of sale' application.
    """,

    'depends': ['point_of_sale', 'maison_custom'],

    'data': [
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_maison/static/src/**/*',
        ],
    },
    'license': 'LGPL-3',
}
