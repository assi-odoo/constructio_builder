from odoo import models,fields

class Material(models.Model):
    _name="material.stock"
    _description="all materials we have or not available in quantity"

    name = fields.Char()
    quantity= fields.Integer()
    price = fields.Integer()