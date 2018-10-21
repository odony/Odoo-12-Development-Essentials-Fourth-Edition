from odoo import fields, models


class Stage(models.Model):
    _name = 'library.borrow.stage'
    _description = 'Borrowing Stage'
    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer()
    state = fields.Selection(
        [('draft', 'New'),
         ('open', 'Borrowed'),
         ('done', 'Returned'),
         ('lost', 'Lost'),
         ('cancel', 'Cancelled')],
        'State'])
