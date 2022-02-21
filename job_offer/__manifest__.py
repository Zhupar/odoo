# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Recruitment',
    'version': '13.0.1.0.0',
    'summary': 'Job Offer Summary',
    'category': 'Productivity',
    'sequence': -100,
    'description': ' Job offer description',
    'website': 'www.example.com',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/menu.xml',
        'views/hr_applicant.xml',
        'views/job_positions.xml',
        'views/responsibilities.xml',
        'views/hr_offer.xml',

    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    
    'license': 'LGPL-3',
}
