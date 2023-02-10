from odoo import fields,models
from dateutil.relativedelta import relativedelta

class ConstructionOrders(models.Model):
    _name= "construction.orders"
    _description="creating a section for listing all product which is going to used in this projects.."

    vendor = fields.Char(required=True)
    quantity = fields.Integer(required=True)
    material = fields.Char(required=True)
    expected_delivery = fields.Date(copy=False,default= lambda self: fields.Datetime.now()+relativedelta(month=1))

    