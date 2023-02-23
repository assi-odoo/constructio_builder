from odoo import models,fields,api
from odoo.exceptions import ValidationError

class Material(models.Model):
    _name="material.stock"
    _description="all materials we have or not available in quantity"

    name = fields.Char()
    quantity= fields.Integer()
    price = fields.Integer()
    orders_ids=fields.One2many("construction.orders","material_ids")
    

    _sql_constraints = [
        ('check_Unique', 'unique(name)',
         'Material must be unique')]

    @api.constrains('price')
    def _restrict_total_price(self):
        for record in self:
            if record.price < 0:
                raise ValidationError("Total Price Can't be less then 0.")