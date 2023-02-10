from odoo import models,fields

class ConstrProperty(models.Model):
    _name = 'construction.property'
    _description = 'Building a construction managing application for business'

    site_name = fields.Char(required=True)
    description = fields.Char()
    customer_name = fields.Char(required=True)
    location = fields.Char(required=True)
    area = fields.Integer(required=True)
    construction_type = fields.Selection(
        selection = [('house','House'),('residential building','Residential Building'),
        ('commercial','Commercial'),('heavy civil construction', 'Heavy Civil Construction')])
    state = fields.Selection(
        selection = [('planning','Planning'),('preconstruction','Preconstruction'),
        ('construction','Construction'),('close-out','Close-Out')],copy=False)
    assign_to=fields.Char()
    workers = fields.Integer(required=True)
    
    