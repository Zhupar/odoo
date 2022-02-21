from odoo import api, fields, models, _


class HROffer(models.Model):
    _name = 'hr.offer'
    _description = 'HR Offer'
    applicant_id = fields.Many2one('hr.applicant', string="Applicant's name")
    position_id = fields.Many2one('hr.job', string="Position")
    reference = fields.Char(string='Number', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    schedule_start = fields.Datetime(string="Start Work", related="position_id.date_start")
    schedule_end = fields.Datetime(string="Finish Work", related="position_id.date_end")

    city = fields.Char(string="City", related="position_id.address")
    company = fields.Char(string="Company", related="position_id.name_of_company")
    manager = fields.Char(string="Position Manager", related="position_id.position_manager")
    salary = fields.Char(string="Salary", required=True)
    premium = fields.Char(string='Premium')
    employment = fields.Selection(string='Employment', related='position_id.employment')
    job_type = fields.Selection(string='Type', related='position_id.job_type')
    trial_period = fields.Char(string="Trial Period")
    offer_date = fields.Date(string="Offer Date")
    expiry_date = fields.Date(string='Offer expiry date')
    prepared_by = fields.Char(string="Prepared By")
    insurance = fields.Boolean(string='insurance', related='position_id.insurance', required=True)
    paid_holiday = fields.Boolean(string='paid_holiday', related='position_id.paid_holiday')
    add_paid_holiday = fields.Boolean(string='add_paid_holiday', related='position_id.add_paid_holiday')

    state = fields.Selection([('new', 'New'), ('progress', 'In Progress'), ('employee', 'Send To Employee'),
                              ('signed', 'Signed')],
                             default='new', string='Status', tracking=True)
    number_of_days = fields.Integer(string="Number Of Days")
    add_number_of_days = fields.Integer(string="Number Of Days")
    responsibilities_id = fields.Many2many('hr.job.responsibility', string="resp", related='position_id.job_responsibilities_ids')

    def action_send_employee(self):
        self.state = 'employee'

    def action_signed(self):
        self.state = 'signed'
    

    @api.model
    def create(self, vals):

        if vals.get('reference', _('New') == _('New')):
            vals['state'] = 'progress'
            vals['reference'] = self.env['ir.sequence'].next_by_code('hr.offer') or _('New')

        res = super(HROffer, self).create(vals)
        return res





class JobResponsibility(models.Model):
    _name = 'hr.job.responsibility'
    _description = 'Job Responsibility'
    name = fields.Char(string="Responsibility")










