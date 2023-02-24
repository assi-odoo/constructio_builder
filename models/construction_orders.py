from odoo import fields,models,api,_
from dateutil.relativedelta import relativedelta

class ConstructionOrders(models.Model):
    _name= "construction.orders"
    _description="creating a section for listing all product which is going to used in this projects.."
    _rec_name="vendor"
    _order="total desc"

    vendor = fields.Many2one('res.partner',required=True)
    material_ids = fields.Many2many("material.stock")
    expected_delivery = fields.Date(copy=False,default= lambda self: fields.Datetime.now()+relativedelta(days=12))
    total = fields.Integer(default=0,compute="_total_price_material")
    # construction_material_ids= fields.One2many("material.stock","orders_id")    you can't Point TWO field point at the same model
    for_site = fields.Many2one("construction.property")

    @api.depends("material_ids")
    def _total_price_material(self):
        for record in self:
            # record.total = record.total+record.material_ids.price
            record.total = sum(record.material_ids.mapped("price")) 
   








