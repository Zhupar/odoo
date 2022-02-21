from odoo import api, fields, models, _


class Job(models.Model):
    _name = 'hr.job'
    _description = 'Job Positions'
    name = fields.Char(string='Name', required=True)
    address = fields.Char(string='Address', required=True)
    name_of_company = fields.Char(string='Company', required=True)
    position_manager = fields.Char(string='Job position Manager', required=True)
    employment = fields.Selection([
        ('full-time', 'full-time'),
        ('part-time', 'part-time'),
        ('flexible schedule', 'flexible schedule'),
    ], required=True)
    date_start = fields.Datetime(string="Start Work")
    date_end = fields.Datetime(string="Finish Work")

    job_type = fields.Selection([
        ('temporary', 'temporary'),
        ('project', 'project'),
        ('seasonal', 'seasonal'),
        ('rotational', 'rotational'),
        ('constant', 'constant'),
    ], required=True)

    job_responsibilities_ids = fields.Many2many('hr.job.responsibility', string="Responsibilities")
    insurance = fields.Boolean(string="Insurance")
    paid_holiday = fields.Boolean(string="Paid_Holiday")
    add_paid_holiday = fields.Boolean(string="Additional Paid Holiday")