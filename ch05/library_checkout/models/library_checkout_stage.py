from odoo import fields, models


class Stage(models.Model):
    _name = 'library.checkout.stage'
    _description = 'Checkout Stage'
    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer()
    state = fields.Selection(
        [('draft', 'New'),
         ('open', 'Borrowed'),
         ('done', 'Returned'),
         ('lost', 'Lost'),
         ('cancel', 'Cancelled')],
        'State')
