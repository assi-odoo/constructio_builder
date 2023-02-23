from odoo import models,fields
from odoo.exceptions import UserError,ValidationError

class ConstrProperty(models.Model):
    _name = 'construction.property'
    _description = 'Building a construction managing application for business'
    rec_name="Construction name"

    site_name = fields.Char(required=True)
    description = fields.Char()
    customer_name = fields.Many2one("res.users")
    location = fields.Char(required=True)
    area = fields.Integer(required=True)
    construction_type = fields.Selection(
        selection = [('house','House'),('residential building','Residential Building'),
        ('commercial','Commercial'),('heavy civil construction', 'Heavy Civil Construction')])
    state = fields.Selection(
        selection = [('new','New'),('planning','Planning'),
        ('construction','Construction'),('close-out','Close-Out')],copy=False)
    assign_to=fields.Char(required=True)
    workers = fields.Integer(required=True)
    
            # Finished Button Logic
    def finish_action_button(self):
        for record in self:
            if record.state != 'close-out':
                raise UserError("Construction are being in process can't be Finished Yet.")
            # Cancel Button Logic
    def cancel_action_button(self):
        for record in self:
            if record.state == 'close-out':
                raise UserError("Finished Sites can't be canceled")



