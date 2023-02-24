from odoo import fields,models

class ConstructionDepartment(models.Model):
    _name="construction.department"
    _description = "Department assign to each manager in site ande employee"
    _rec_name = "department"

    manager = fields.Char(required=True)
    department = fields.Selection(
        selection = [('project manager office','Project Manager Office'),
        ('engineering survey department','Engineering Survey Department.'),
        ('construction department','Construction Department.'),
        ('budget and construction organization department.','Budget and Construction Organization Department.'),
        ('hvac, utility and technology department.','HVAC, Utility and Technology Department.')])
    location = fields.Char()
    Workers =fields.Integer()



    