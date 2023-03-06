from odoo import models,fields
from odoo.exceptions import UserError,ValidationError

class ConstrProperty(models.Model):
    _name = 'construction.property'
    _description = 'Building a construction managing application for business'
    _rec_name="site_name"
    _order="id desc"

    site_name = fields.Char(required=True)
    description = fields.Char()
    customer_name = fields.Char(required=True)
    location = fields.Char()
    area = fields.Integer()
    construction_type = fields.Selection(
        selection = [('house','House'),('residential building','Residential Building'),
        ('commercial','Commercial'),('heavy civil construction', 'Heavy Civil Construction')])
    state = fields.Selection(
        selection = [('new','New'),('planning','Planning'),
        ('construction','Construction'),('close-out','Close-Out'),('cancel','Cancel')],copy=False,default='new')
    assign_to=fields.Many2one("res.users")
    workers = fields.Integer()
    sequence = fields.Integer("Sequence",default=1, help="Used to order stages. Lower is better.")


    _sql_constraints=[(
        'worker_size_positive','CHECK(workers>0)',
        'Worker size must be more than 1, mention inside other informations')]

            # Finished Button Logic
    def finish_action_button(self):
        for record in self:
            if record.state =='cancel':
                raise UserError("Finished Sites can't be canceled")
            else:
                self.state = 'close-out'

            # Cancel Button Logic
    def cancel_action_button(self):
        for record in self:
            if record.state == 'close-out':
                raise UserError("Finished Sites can't be canceled")
            else:
                self.state='cancel'
                


