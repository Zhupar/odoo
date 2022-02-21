from odoo import api, fields, models, _


class JobApplicant(models.Model):
    _name = 'hr.applicant'
    _description = 'HR applicant'
    name = fields.Char(string='Name', required=True)
    email = fields.Char(string="E-mail")
    mobile_phone = fields.Char(string='Phone', required=True)
    degree = fields.Text(string='Degree')
    related_offer_id = fields.One2many('hr.offer', 'applicant_id', string='Related Offers')

    def action_create_offer(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Offer',
            'view_type': 'form',
            'view_id': False,
            'res_model': 'hr.offer',
            'view_mode': 'form',
            'domain': [],
            'context': "{'create': True, 'default_applicant_id': active_id}"
        }